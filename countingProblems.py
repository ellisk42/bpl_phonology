# -*- coding: utf-8 -*-

from result import *
from features import FeatureBank, tokenize
from latex import latexWord
from rule import *
from morph import Morph
from sketch import *
from solution import *
from utilities import *

class CountingProblem():
    def __init__(self, data, count, problemName=None):
        self.problemName = problemName
        self.data = [ Morph(tokenize(x)) for x in data ]
        self.count = count
        self.bank = FeatureBank([ w for w in data ])

        self.maximumObservationLength = max([ len(w) for w in self.data ]) + 1

    def latex(self):
        r = "\\begin{tabular}{ll}\n"
        for k,o in zip(self.count, self.data):
            if k < 11:
                r += "%d&%s\\\\\n"%(k,latexWord(o))
            elif k%10 == 0:
                r += "%d = %d + 10 & %s\\\\\n"%(k,k/10,latexWord(o))
            elif k < 20:
                r += "%d = 10 + %d & %s\\\\\n"%(k,k-10,latexWord(o))
            else:
                assert False
        r += "\n\\end{tabular}\n"
        return r

    def expandFrontier(self, s, k):
        ss = [s]
        for _ in range(k-1):
            ss.append(self.sketchJointSolution(1, canAddNewRules = True, existingSolutions = ss))
        return Frontier([ [solution.rules[0] for solution in ss ] ],
                        prefixes = s.prefixes,
                        suffixes = s.suffixes,
                        underlyingForms = s.underlyingForms)
        

    def sketchJointSolution(self, depth, canAddNewRules = True, existingSolutions = []):
        assert depth == 1
        assert canAddNewRules

        Model.Global()

        r = Rule.sample()
        for o in existingSolutions:
            assert len(o.rules) == 1
            condition(Not(ruleEqual(r, o.rules[0].makeConstant(self.bank))))

        morphs = {}
        morphs[1] = Morph.sample()
        morphs[4] = Morph.sample()
        morphs[5] = Morph.sample()
        morphs[9] = Morph.sample()
        morphs[10] = Morph.sample()

        if existingSolutions:
            for (k,),v in existingSolutions[0].underlyingForms.iteritems():
                condition(wordEqual(v.makeConstant(self.bank),
                                    morphs[k]))

        for j in range(len(self.data)):
            o = self.data[j]
            k = self.count[j]
            if k <= 10:
                condition(wordEqual(o.makeConstant(self.bank),
                                    applyRule(r,morphs[k], Constant(0), self.maximumObservationLength)))
            elif k%10 == 0:
                condition(wordEqual(o.makeConstant(self.bank),
                                    applyRule(r,concatenate(morphs[k/10], morphs[10]),
                                              Constant(0), self.maximumObservationLength)))
            elif k < 20:
                condition(wordEqual(o.makeConstant(self.bank),
                                    applyRule(r,concatenate(morphs[10], morphs[k - 10]),
                                              Constant(0), self.maximumObservationLength)))
            else:
                assert False

        minimize(ruleCost(r))

        try:
            output = solveSketch(self.bank,
                                 unroll = self.maximumObservationLength + 2,
                                 maximumMorphLength = self.maximumObservationLength + 1)
        except SynthesisFailure:
            print "Failed at phonological analysis."
            return None

        r = Rule.parse(self.bank, output, r)
        print r.pretty()
        return Solution(rules = [r],
                        prefixes = [], suffixes = [],                        
                        underlyingForms = {(k,): Morph.parse(self.bank, output, m) for k,m in morphs.iteritems() })

