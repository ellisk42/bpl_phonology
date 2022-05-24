# -*- coding: utf-8 -*-

from utilities import *
from Marcus import *
from supervised import SupervisedProblem
from problems import *
from matrix import *
from parseSPE import *
from incremental import *
from features import *
from fragmentGrammar import *
from command_server import start_server


TESTS = []
def test(f):
    TESTS.append(f)
    return f

@test
def place():
    data = [(u"man", u"mank"),
            (u"b", u"gk"),
            (u"t", u"kk"),
            (u"z",u"gk")]
    solver = UnderlyingProblem(data)
    enableGeometry()
    solution1 = solver.sketchJointSolution(1)
    disableGeometry()
    solution2 = solver.sketchJointSolution(1)
    assert isinstance(solution1.rules[0].structuralChange, PlaceSpecification)
    assert not isinstance(solution2.rules[0].structuralChange, PlaceSpecification)
    assert solution1.cost() < solution2.cost()
    
@test
def features():
    collisions = []
    for p in featureMap:
        for q in featureMap:
            if p == q: continue
            
            if not (set(featureMap[p]) != set(featureMap[q])):
                print "WARNING: %s and %s have the same features"%(p,q)
                collisions.append((p,q))
    for problem in alternationProblems + MATRIXPROBLEMS:
        if isinstance(problem,str): continue
        
        if not isinstance(problem.data[0],unicode):
            words = set(w for x in problem.data for w in x if w != None)
        else:
            words = problem.data

        inventory = set(p for w in words for p in tokenize(w))
        for (p,q) in collisions:
            if p in inventory and q in inventory:
                print "In problem:"
                print problem.description
                print "We have the collision:"
                print p,q
                assert False

    F = set(f for fs in featureMap.values() for f in fs)
    P = featureMap.keys()
    for f in F:
        collision = any([ (set(featureMap[q]) - set([f])) == (set(featureMap[p]) - set([f]))
                          for j,p in enumerate(P[:-1])
                          for q in P[j+1:] ])
        if not collision: print "Looks like you can safely remove feature ",f
                
        

@test
def editSequences():
    assert len(everyEditSequence([0,1],[1,2],allowSubsumption = True)) > \
        len(everyEditSequence([0,1],[1,2],allowSubsumption = False))
    bounded = everyEditSequence([0,1],[1,2],allowSubsumption = False,maximumLength = 2)
    unbounded = everyEditSequence([0,1],[1,2],allowSubsumption = False,maximumLength = None)
    assert len(unbounded) > len(bounded)
    assert len(bounded) == 1
    assert len(everyEditSequence([0,1,2],[1,2],allowSubsumption = False)) == 16
@test
def useUniversal():
    ug = FragmentGrammar.load('universalGrammars/groundTruth.p')
    s = UnderlyingProblem(underlyingProblems[1].data, UG = ug).sketchJointSolution(1, canAddNewRules = False)
    s.modelCost(ug)
@test
def learnUniversal():
    ug = getEmptyFragmentGrammar()
    for p in MATRIXPROBLEMS:
        if isinstance(p,Problem) and p.solutions != []:
            for s in p.solutions:
                # See if we can evaluate the likelihood
                s = parseSolution(s)
                assert isFinite(s.modelCost(ug))

                # See if we can learn the parameters
                frontiers = [ [r] for r in s.rules ]
                beforeLearning = ug.frontiersLikelihood(frontiers)
                learnedGrammar = ug.estimateParameters(frontiers)
                afterLearning = learnedGrammar.frontiersLikelihood(frontiers)
                assert afterLearning > beforeLearning

                # See if we can learn the structure
                structure = induceFragmentGrammar(frontiers, smoothing = 0.0).estimateParameters(frontiers)
                assert structure.frontiersLikelihood(frontiers) >= afterLearning
                
    
@test
def spread():
    s = UnderlyingProblem(sevenProblems[1].data)
    assert s.applyRuleUsingSketch(parseRule("a > e/#CC*_"), Morph(u"kkaek"),0) == Morph(u"kkeek")
    assert s.applyRuleUsingSketch(parseRule("a > e/CC*_"), Morph(u"kkaek"),0) == Morph(u"kkeek")
    assert s.applyRuleUsingSketch(parseRule("a > e/#CC_"), Morph(u"kkaek"),0) == Morph(u"kkeek")
    assert s.applyRuleUsingSketch(parseRule("a > e/#C_"), Morph(u"kaek"),0) == Morph(u"keek")
@test
def deleteInitial():
    s = UnderlyingProblem([[u"katigtde"]])
    assert  s.applyRuleUsingSketch(parseRule("C > 0/#_"), Morph(u"kat"),0) == Morph(u"at")
    assert  s.applyRuleUsingSketch(parseRule("C > 0/#_"), Morph(u"ekat"),0) == Morph(u"ekat")
    assert  s.applyRuleUsingSketch(parseRule("V > 0/#_"), Morph(u"ekat"),0) == Morph(u"kat")
@test
def supervisedDeleteInitial():
    s = SupervisedProblem([(Morph("kat"),0,Morph("at"))])
    r = s.solve(1)[0]
    assert isinstance(r.structuralChange, EmptySpecification)
    s = SupervisedProblem([(Morph("kat"),0,Morph("at")),
                           (Morph("dat"),0,Morph("at")),
                           (Morph("fat"),0,Morph("at")),
                           (Morph("rat"),0,Morph("at")),
                           (Morph("iat"),0,Morph("iat")),
                           (Morph(u"ɩat"),0,Morph(u"ɩat")),
                           (Morph("oat"),0,Morph("oat"))])
    r = s.solve(1)[0]
    assert isinstance(r.structuralChange, EmptySpecification)
    assert isinstance(r.focus, FeatureMatrix)
    assert str(r.focus) == "[ -vowel ]"
@test
def supervisedOptionalEndOfString():
    # Intended rule: m > n/_{#,t}
    s = SupervisedProblem([(Morph("man"),0,Morph("man")),
                           (Morph("kamt"),0,Morph("kant")),
                           (Morph("kamk"),0,Morph("kamk")),
                           (Morph("kamd"),0,Morph("kamd")),
                           (Morph("om"),0,Morph("on")),
                           (Morph("mta"),0,Morph("nta")),
                           (Morph("iatm"),0,Morph("iatn"))])
    r = s.solve(1)[0]
    assert unicode(r.rightTriggers) == u'{#,t}'
    assert len(r.leftTriggers.specifications) == 0
    assert not r.leftTriggers.endOfString
@test
def supervisedDuplicateSyllable():
    s = SupervisedProblem([(Morph("xa"),0,Morph("xaxa"))],
                          syllables = True)
    r = s.solve(1)[0]
    assert isinstance(r.focus, EmptySpecification)
    assert isinstance(r.structuralChange,OffsetSpecification)
    assert r.structuralChange.offset == 1 and unicode(r.rightTriggers.specifications[0]) == u'σ'\
        or r.structuralChange.offset == -1 and unicode(r.leftTriggers.specifications[0]) == u'σ'
@test
def testMarcus():
    data = [ (w,) for w in sampleABB(6) ]
    s = UnderlyingProblem(data,
                          useSyllables = True)
    s.fixedMorphology = [(Morph([]),Morph([]))]
    s = s.sketchJointSolution(1,canAddNewRules = True)
    assert len(s.rules) == 1
    assert any([ unicode(spec) == u'σ'
                 for spec in s.rules[0].rightTriggers.specifications + s.rules[0].leftTriggers.specifications ])
    assert all([ len(u) == 4 for u in s.underlyingForms.values() ])
    assert isinstance(s.rules[0].structuralChange, OffsetSpecification)
@test
def induceBoundary():
    inventory = FeatureBank([u"utestadz"])
    Model.Global()
    r = Rule.sample()
    condition(FunctionCall("rule_uses_boundary",[r]))
    # stem = ute
    # suffix = st
    prefix = Morph([]).makeConstant(inventory)
    stem = Morph(u"ute").makeConstant(inventory)
    suffix = Morph(u"st").makeConstant(inventory)
    x = concatenate3(prefix, stem, suffix)
    y = Morph(u"utezt").makeConstant(inventory)
    prediction = applyRules([r,r,r], x, wordLength(prefix) + wordLength(stem), 6)
    auxiliaryCondition(wordEqual(prediction, y))

    minimize(ruleCost(r))

    output = solveSketch(inventory)
    g = Rule.parse(inventory,output,r).leftTriggers.specifications
    assert len(g) == 1
    assert isinstance(g[0],BoundarySpecification)
    
@test
def suffixBoundary():
    problem = Problem.named["Odden_4.2_Standard_Ukrainian"]
    data = problem.data[:3] + problem.data[5:6]
    s = IncrementalSolver(problem.data,2).restrict(data)
    solution = parseSolution(''' + stem + 
 + stem + am
 + stem + ov^yi
 + stem + i
 + stem + ov^yi
 + stem + 
 + stem + 
 + stem + 
 + stem + 
 + stem + 
C > [+palletized] / _ i ;; i is the only thing in the data which is [+high -back]
o > e / [+palletized] + _ ;; i is the only thing that is [+vowel +high -back]. "vowel fronting"
[ -glide -vowel ] ---> [ -palletized ] /  _ e
''')
    s.fixedMorphology = zip(solution.prefixes, solution.suffixes)
    new = s.sketchChangeToSolution(solution, [solution.rules[0],None,solution.rules[2]])
    assert new is not None, "Should be able to incrementally change to accommodate an example"
    assert new.cost() <= solution.cost(), "Should have found an optimal solution"
    for d in data:
        assert s.verify(solution, [Morph(x) if x != None else None
                                   for x in d]), "Could not verify ground truth solution"
        assert s.verify(new, [Morph(x) if x != None else None
                              for x in d]), "Could not verify learned solution"

@test
def Gemini():
    data = [(u"tes",u"tessi"),
            (u"tes",u"tesi"),
            (u"ak",u"akki"),
            (u"lof",u"loffi"),
            (u"pig",u"pigi")]
    solver = UnderlyingProblem(data)
    try:
        solution = solver.sketchJointSolution(1)
        assert len(solution.rules) == 1
        assert solution.rules[0].isGeminiRule()
    except SynthesisFailure:
        assert False, "Could not solve Gemini test"

@test
def verify():
    for p in sevenProblems[:3] + [interactingProblems[4]] + interactingProblems[:3] + underlyingProblems[:6] + underlyingProblems[7:]:
        solver = UnderlyingProblem(p.data)
        for s in p.solutions:
            s = parseSolution(s)
            for x in solver.data:
                if not solver.verify(s,x):
                    print "Error in verifying solution:"
                    print s
                    print "To problem:"
                    print p.description
                    print "Could not verify %s"%(u" ~ ".join(map(unicode,x)))
                    assert False
            
if __name__ == "__main__":
    import sys
    import time
    start_server(1)
    
    startTime = time.time()
    A = sys.argv
    if len(A) > 1:
        for f in A[1:]:
            print " [+] Running test",f
            eval('%s()'%f)
    else:
        for f in TESTS:
            print " [+] Running test",f.__name__
            f()
            print
    print "\nTotal time taken by unit tests",time.time() - startTime
    print "Total solver time taken by unit tests",getGlobalSketchTime()
