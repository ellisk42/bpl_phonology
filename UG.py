# -*- coding: utf-8 -*-


from problems import Problem
from rule import *
from utilities import *
from fragmentGrammar import *
from time import time
import re
import math
#import matplotlib.pyplot as plot
import pickle
import os
from random import random
import cProfile
from textbook_problems import *
from problems import MATRIXPROBLEMS


def worker(arguments):
    eq = [] # list of equivalence classes
    frontiers = [] # Frontiers that might be adjusted
    problems = [] # Problems that those frontiers came from
    for source in arguments.load:
        if source in Problem.named:
            problem = Problem.named[source]
            if isinstance(problem,Problem):
                if len(problem.solutions) == 0:
                    print "Could not find any ground truth solutions for",source
                    continue

                if len(problem.solutions) > 1:
                    print "Found multiple ground truth solutions for",source,"going with the first one..."
                    
                s = parseSolution(problem.solutions[0]).rules
                print "Loading",len(s),"rules from",source
                for r in s:
                    eq.append([r])
            else:
                print "Does not seem to be a problem instance:",source
                assert False, "make sure that the problems and checkpoints were giving me actually exist"
                
        else:
            try:
                result = loadPickle(source)
            except:
                assert False, "Failure loading %s"%source
            frontier = result.finalFrontier.makeGeometric()
            for rs in frontier.frontiers:
                for r in rs:
                    if isinstance(r.structuralChange,PlaceSpecification):
                        g = r.leftTriggers if r.structuralChange.offset < 0 else r.rightTriggers
                        if g.optionalEnding:
                            print "FAILURE",r,source
            frontiers.append(frontier)
            problems.append(result.problem)
            print "Loading",len(frontier.frontiers),"rule equivalence classes from",source
            MAP = frontier.MAP().rules
            for rs,r in zip(frontier.frontiers,MAP):
                rs = [aRule for aRule in rs
                      if not any( anotherRule < aRule for anotherRule in rs )]
                print "frontier size",len(rs),"MAP",r
                eq.append(rs)
                print "alternatives..."
                for r in sorted(eq[-1],key=lambda rrr: rrr.cost()):
                    print r
                    
                    # fragment = RuleFragment.abstract(r,r)
                    # if len(fragment) == 0:
                    #     print("no fragments")
                    #     continue
                    
                    # fragment = fragment[0]
                    # g = getEmptyFragmentGrammar()
                    # print g.fragmentPrior(fragment,g.ruleFragments)
                    # print g.ruleLogLikelihood(r)[0]
                print 

    
    g = induceFragmentGrammar(eq, CPUs=arguments.CPUs,
                              priorWeight=arguments.priorWeight,
                              smoothing=arguments.smoothing,
                              restore=arguments.restore)
    for frontier, problem in zip(frontiers, problems):
        print "Problem",problem,"is solved by the following solution according to this UG:"
        solution = frontier.MAP(g)
        solution.underlyingForms = {}
        print solution
        print 

    

    
    if arguments.export != None:
        exportPath = arguments.export
        print "Exporting universal grammar to %s"%(exportPath)
        g.export(exportPath)

    

if __name__ == '__main__':
    import argparse
    from parseSPE import parseSolution

    parser = argparse.ArgumentParser(description = 'Infer probabilistic grammars over phonological rules')
    parser.add_argument('--export', type = str, default = None)
    parser.add_argument('load', type = str, default = [], nargs='+',
                        help="This is a list of problems / paths to experiment outputs.")
    parser.add_argument('--CPUs', type = int, default = numberOfCPUs())
    parser.add_argument('--restore', default=None,
                        help="restore grammar induction from a checkpoint")
    parser.add_argument('--empty', default=False, action='store_true',
                        help="allow the empty feature matrix to be part of UG")
    parser.add_argument('--priorWeight',default=1.,type=float)
    parser.add_argument('--smoothing',default=1.,type=float)
    
    arguments = parser.parse_args()
    if arguments.empty: enableUniversalEmpty()

    worker(arguments)
    
