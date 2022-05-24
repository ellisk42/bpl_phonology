# -*- coding: utf-8 -*-

from compileRuleToSketch import compileRuleToSketch
from utilities import *
from solution import *
from features import FeatureBank, tokenize
from rule import * # Rule,Guard,FeatureMatrix,EMPTYRULE
from morph import Morph
from sketchSyntax import Expression,makeSketchSkeleton
from sketch import *
from supervised import SupervisedProblem
from latex import latexMatrix
from problems import *

from pathos.multiprocessing import ProcessingPool as Pool
import random
import sys
import pickle
import math
from time import time
import itertools
import copy

        

class AlignmentProblem(object):
    def __init__(self, data, CPUs=1):
        self.CPUs = CPUs
        self.bank = FeatureBank([ w for l in data for w in l if w != None ] + [u'?',u'*'])
        self.numberOfInflections = len(data[0])
        # wrap the data in Morph objects if it isn't already
        self.data = [ tuple( None if i == None else (i if isinstance(i,Morph) else Morph(tokenize(i)))
                             for i in Lex)
                      for Lex in data ]

        self.maximumObservationLength = max([ len(w) for l in self.data for w in l if w != None ])


    def solveSketch(self, minimizeBound = 31, maximumMorphLength=None):
        if maximumMorphLength is None: maximumMorphLength = self.maximumObservationLength
        return solveSketch(self.bank,
                           # unroll: +1 for extra UR size, +1 for guard buffer
                           self.maximumObservationLength + 2,
                           # maximum morpheme size
                           maximumMorphLength,
                           showSource = False, minimizeBound = minimizeBound)

    def solveAlignment(self):
        Model.Global()
        prefixes = [Morph.sample() for _ in range(self.numberOfInflections) ]
        suffixes = [Morph.sample() for _ in range(self.numberOfInflections) ]
        stems = [Morph.sample() for _ in self.data ]

        for surfaces,stem in zip(self.data, stems):
            for (p,s),x in zip(zip(prefixes, suffixes),surfaces):
                if x is None: continue
                condition(matchPattern(x.makeConstant(self.bank),
                                       concatenate3(p,stem,s)))

        for i in range(self.numberOfInflections):
            if all( ss[i] == None for ss in self.data ):
                condition(wordLength(prefixes[i]) == 0)
                condition(wordLength(suffixes[i]) == 0)

        # OBJECTIVE: (# inflections) * (stem lengths) + (# data points) * (affix len)
        # Because we pay for each stem once per inflection,
        # and pay for each affix once per data point
        observationsPerStem = float(sum(s is not None
                                        for ss in self.data
                                        for s in ss )) / len(stems)
        observationsPerAffix = sum( sum(ss[i] is not None
                                        for ss in self.data )
                                    for i in range(self.numberOfInflections) ) \
                                        / float(self.numberOfInflections)
        print "observations per stem",observationsPerStem
        print "observations per affix",observationsPerAffix

        r = observationsPerStem/observationsPerAffix
        if r < 2 and r > 0.5:
            ca = 1
            cs = 1
        elif r >= 2:
            ca = 1
            cs = 2
        elif r <= 0.5:
            ca = 2
            cs = 1
        else: assert False

        print "ca = ",ca
        print "cs = ",cs
            
        minimize(sum((patternCost(p) + patternCost(s)) * ca
                     for j,(p,s) in enumerate(zip(prefixes, suffixes))) + \
                 sum(patternCost(stem) * cs
                     for stem,ss in zip(stems, self.data) ))
        # for m in prefixes + suffixes:
        #     condition(patternCost(m) < 4)

        output = self.solveSketch()
        solution = Solution(rules=[],
                            prefixes=[Morph.parse(self.bank, output, p) for p in prefixes ],
                            suffixes=[Morph.parse(self.bank, output, p) for p in suffixes ],
                            underlyingForms={x: Morph.parse(self.bank, output, s)
                                             for x,s in zip(self.data, stems) })

        for i in range(self.numberOfInflections):
            if all( ss[i] == None for ss in self.data ):
                print("\t(inflection not seen)")
            else:
                print solution.prefixes[i],"+ stem +",solution.suffixes[i]
        return solution

    def restrict(self, newData):
        restriction = copy.copy(self)
        restriction.data = [ tuple( None if i == None else (i if isinstance(i,Morph) else Morph(tokenize(i)))
                               for i in Lex)
                             for Lex in newData ]
        return restriction

    def solveStem(self, ss, morphology):
        Model.Global()
        stem = Morph.sample()

        for (p,s),x in zip(zip(morphology.prefixes,
                               morphology.suffixes),
                           ss):
            if x is None: continue

            condition(matchPattern(x.makeConstant(self.bank),
                                   concatenate3(p.makeConstant(self.bank),
                                                stem,
                                                s.makeConstant(self.bank))))

        minimize(patternCost(stem))
        output = self.solveSketch()
        return Morph.parse(self.bank, output, stem)

    def solutionCost(self, solution):
        def patternCost(m):
            cost = 0
            for p in m.phonemes:
                if p == u'?': cost += 2
                elif p == u'*': cost += 1
            return cost
        failures = 0
        totalCost = 0
        for ss in self.data:
            if not (ss in solution.underlyingForms):
                failures += 1
                continue
            
            for i in range(self.numberOfInflections):
                if ss[i] is None: continue
                u = solution.prefixes[i] + solution.underlyingForms[ss] + solution.suffixes[i]
                totalCost += patternCost(u)
        return totalCost
                

    def guessMorphology(self, batchSizes, numberOfSamples):
        from random import choice
        
        # For each inflection usage pattern, collect those data points that use inflections in that way
        def pattern(ss): return tuple(s is not None for s in ss )
        inflectionUsagePatterns = { pattern(ss)
                                    for ss in self.data }
        patternUsers = { p: [ss for ss in self.data if pattern(ss) == p ]
                         for p in inflectionUsagePatterns }
        batches = []
        for _ in range(numberOfSamples):
            this = []
            for p, users in patternUsers.items():
                bs = random.choice(batchSizes)
                data = randomlyPermute(users)[:bs]
                this += data
            batches.append(this)

        def morphologyBatch(b):
            try:
                s = self.restrict(b).solveAlignment()
            except SynthesisFailure: return None
            s.underlyingForms = {}
            return s            

        solutions = lightweightParallelMap(self.CPUs, morphologyBatch, batches)
        solutions = {s for s in solutions if s is not None }
        print "Got",len(solutions),"distinct solutions"
        solutions = list(solutions)

        def underlyingBatch(s):
            for ss in self.data:
                try:
                    s.underlyingForms[ss] = self.solveStem(ss, s)
                except SynthesisFailure: pass
            return s
        solutions = lightweightParallelMap(self.CPUs, underlyingBatch, solutions)
        
        for s in solutions:
            print("SOLUTION")
            print s
            print "Accounts for",float(len(s.underlyingForms))/len(self.data),"of the data"
            print "COST",self.solutionCost(s)
            print 

        goodSolutions = [s for s in solutions
                         if len(s.underlyingForms) > 0.9*len(self.data)]
        if len(goodSolutions) == 0:
            print "FAILURE: none of the solutions are very good"
            return None

        best = min(solutions,
                   key = lambda s: self.solutionCost(s))
        return best                
        
        
        


if __name__ == "__main__":
    from command_server import start_server, kill_servers
    import os
    import argparse
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument("--CPUs",type=int,
                         default=1)
    parser.add_argument("--start",type=int,
                        default=0)
    arguments = parser.parse_args()
    
    os.system("mkdir  -p precomputedAlignments")
    CPUs = arguments.CPUs
    if CPUs > 1:
        kill_servers()
        
    start_server(CPUs)

    for i,p in enumerate(MATRIXPROBLEMS):
        if i < arguments.start: continue
        
        if not isinstance(p,Problem): continue
        if p.parameters is not None: continue
        solver = AlignmentProblem(p.data, CPUs=CPUs)
        if solver.numberOfInflections == 1: continue
        
        print p.description

        a = solver.guessMorphology(list(range(4,11)),
                                   20)
        print a
        fn = "precomputedAlignments/"+str(i)+".p"
        dumpPickle(a, fn)
        print "exported alignment to",fn
        print
    
