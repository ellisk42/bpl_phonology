# -*- coding: utf-8 -*-


from features import FeatureBank, tokenize
from rule import Rule
from morph import Morph
from sketch import *
from solution import *

class SupervisedProblem():
    def __init__(self, examples, bank = None, syllables = False, problemName=None,
                 UG=None):
        '''examples: either [(Morph, int|Expression, Morph)] or [(Morph, Morph)]
        The inner int|Expression is the distance to the suffix'''

        self.UG = UG

        self.problemName = problemName

        assert len(examples) > 0
        assert all( len(e) == len(examples[0]) for e in examples ),\
            "Supervised examples should all be of the same length"
        if len(examples[0]) == 2:
            examples = [(x,-1,y) for x,y in examples]

        # Convert to morph
        def toMorph(z):
            if isinstance(z,Morph): return z
            elif isinstance(z,(unicode,str)): return Morph(tokenize(z))
            else: assert False
        examples = [(toMorph(x),o,toMorph(y))
                    for x,o,y in examples ]

        # Make it so that the distance to the suffix is always an expression
        examples = [(x, Constant(us) if not isinstance(us,Expression) else us, y) for x,us,y in examples ]
        self.examples = examples
        self.bank = bank if bank != None else \
                    FeatureBank([ w for x,us,y in self.examples for w in [x,y]  ] + ([] if not syllables else [u'-']))
        self.maximumObservationLength = max([len(m) for x,us,y in examples for m in [x,y] ]) + 1
        self.maximumMorphLength = self.maximumObservationLength

    def applyRuleUsingSketch(self,r,u,untilSuffix):
        '''u: morph; r: rule; untilSuffix: int'''
        Model.Global()
        result = Morph.sample()
        _r = r.makeDefinition(self.bank)
        condition(wordEqual(result,applyRule(_r,u.makeConstant(self.bank),
                                             Constant(untilSuffix), len(u) + 2)))
        try:
            output = self.solveSketch(maximumMorphLength=len(u) + 2)
        except SynthesisFailure:
            print "applyRuleUsingSketch: UNSATISFIABLE for %s %s %s"%(u,r,untilSuffix)
            printSketchFailure()
            assert False
        except SynthesisTimeout:
            print "applyRuleUsingSketch: TIMEOUT for %s %s %s"%(u,r,untilSuffix)
            assert False
        return Morph.parse(self.bank, output, result)

    def solveSketch(self, minimizeBound = 31, maximumMorphLength=None):
        if maximumMorphLength is None: maximumMorphLength = self.maximumObservationLength
        return solveSketch(self.bank,
                           # unroll: +1 for extra UR size, +1 for guard buffer
                           self.maximumObservationLength + 2,
                           # maximum morpheme size
                           maximumMorphLength,
                           showSource = False, minimizeBound = minimizeBound)

    def sketchJointSolution(self, d, canAddNewRules=True):
        rules = None
        while rules is None:
            rules = self.solve(d)
            d += 1
        print(rules)
        return Solution(rules=rules,
                        prefixes=[], suffixes=[],
                        underlyingForms={(y,): x
                                         for x,_,y in self.examples})

    def expandFrontier(self, solution, k):
        assert all( len(ps) == 0
                    for ps in solution.prefixes + solution.suffixes )
        
        # construction training data for each rule
        xs = []
        ys = []

        xs.append([x for x,o,y in self.examples ])
        untilSuffix = [o for x,o,y in self.examples]
        CPUs = numberOfCPUs()

        for r in solution.rules:
            ys.append(parallelMap(CPUs, lambda (x,us): self.applyRuleUsingSketch(r,x,us),
                                  zip(xs[-1],untilSuffix) ))
            xs.append(ys[-1])
        for x,y in zip(xs, ys):
            print "Training data for rule:"
            for a,b in zip(x,y):
                print a," > ",b

        # Now that we have the training data, we can solve for each of the rules' frontier
        frontiers = parallelMap(CPUs, lambda (j,r): SupervisedProblem(zip(xs[j],untilSuffix,ys[j]),
                                                                      UG=self.UG).topK(k,r),
                                enumerate(solution.rules))

        return Frontier(frontiers,
                        prefixes = solution.prefixes,
                        suffixes = solution.suffixes,
                        underlyingForms = solution.underlyingForms)
    def topK(self, k, existingRule = None):
        solutions = [] if existingRule == None else [existingRule]

        for _ in range(k - (1 if existingRule else 0)):
            Model.Global()
            rule = Rule.sample()
            for other in solutions:
                condition(ruleEqual(rule, other.makeConstant(self.bank)) == 0)
            
            if self.UG: self.UG.sketchUniversalGrammar(self.bank)            
            minimize(ruleCost(rule))

            for x,us,y in self.examples:
                auxiliaryCondition(wordEqual(applyRule(rule,
                                                       x.makeConstant(self.bank),
                                                       us,
                                                       max(len(x),len(y)) + 1),
                                             y.makeConstant(self.bank)))
            try:
                output = solveSketch(self.bank, self.maximumObservationLength + 1, self.maximumMorphLength)
            except SynthesisFailure:
                print "SupervisedProblem.topK: Only got %d/%d rules."%(len(solutions),k)
                break

            solutions.append(Rule.parse(self.bank, output, rule))
        return solutions

    def solve(self, d):
        Model.Global()
        rules = [ Rule.sample() for _ in range(d) ]
        if self.UG: self.UG.sketchUniversalGrammar(self.bank)
        minimize(sum([ ruleCost(r) for r in rules ]))

        for x,us,y in self.examples:
            auxiliaryCondition(wordEqual(applyRules(rules,
                                                    x.makeConstant(self.bank),
                                                    us,
                                                    max(len(x),len(y)) + 1),
                                         y.makeConstant(self.bank)))
        try:
            output = solveSketch(self.bank, self.maximumObservationLength, self.maximumMorphLength)
        except SynthesisFailure:
            #printLastSketchOutput()
            return None

        return [ Rule.parse(self.bank, output, r)
                 for r in rules ] 

