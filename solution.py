# -*- coding: utf-8 -*-

from sketchSyntax import *
from sketch import *
from utilities import *
from rule import *
from features import *
from fragmentGrammar import getEmptyFragmentGrammar

import math

class AlternationSolution(object):
    def __init__(self, data, substitution, rules, time, frontier=None):
        self.time = time
        self.data = data
        self.substitution = substitution
        self.rules = rules

    def underlyingForms(self):
        return [self.applySubstitution(w) for w in self.data ]
    def applySubstitution(self,w):
        return Morph([self.substitution.get(x,x) for x in w.phonemes])


class Frontier(object):
    def __init__(self, frontiers, prefixes, suffixes, underlyingForms):
        self.frontiers = frontiers
        assert len(prefixes) == len(suffixes)
        self.prefixes = prefixes
        self.suffixes = suffixes
        self.underlyingForms = underlyingForms

        assert isinstance(underlyingForms,dict)

    def merge(self,o):
        assert len(self.prefixes) == len(o.prefixes)
        assert len(self.suffixes) == len(o.suffixes)
        assert all( x == y for x,y in zip(self.prefixes, o.prefixes)  )
        assert all( x == y for x,y in zip(self.suffixes, o.suffixes)  )
        return Frontier(frontiers=[
            list(set(xs)|set(ys))
            for xs,ys in zip(self.frontiers,o.frontiers)
        ],
                        prefixes=self.prefixes,suffixes=self.suffixes,underlyingForms=self.underlyingForms)

    def makeGeometric(self):
        return Frontier([list({r.makeGeometric() for r in rs})
                         for rs in self.frontiers],
                        self.prefixes, self.suffixes, self.underlyingForms)

    def __unicode__(self):
        rs = [ u"rule %d alternatives: \n\t%s"%(j+1,u"\n\t".join(map(unicode,f)))
               for j,f in enumerate(self.frontiers) ]
        return u"\n".join(rs +
                         [self.showMorphology()] +
                         ([u"underlying form: %s ; surfaces = %s"%(u, u" ~ ".join(map(unicode,ss)))
                           for ss,u in self.underlyingForms.iteritems() ]))
    def __str__(self): return unicode(self).encode('utf-8')
    def showMorphology(self):
        lines = []
        for p,s in zip(self.prefixes, self.suffixes):
            x = u"stem"
            if len(p) > 0: x = u"%s + %s"%(p,x)
            if len(s) > 0: x = u"%s + %s"%(x,s)
            lines.append(x)
        return u"\n".join(lines)

    def MAP(self, ug=None):
        def cost(r):
            if ug is None: return r.cost()
            return -ug.ruleLogLikelihood(r)[0]
        return Solution(rules = [ min(f,key = cost)
                                  for f in self.frontiers ],
                        prefixes = self.prefixes, suffixes = self.suffixes,
                        underlyingForms = self.underlyingForms)

        
    
class Solution(object):
    def __init__(self,rules = [],prefixes = [],suffixes = [],underlyingForms = {}):
        assert len(prefixes) == len(suffixes)
        self.rules = rules
        self.prefixes = prefixes
        self.suffixes = suffixes
        self.underlyingForms = underlyingForms

        assert isinstance(underlyingForms,dict)

    def toFrontier(self):
        return Frontier([ [r] for r in self.rules ],
                        prefixes = self.prefixes,
                        suffixes = self.suffixes,
                        underlyingForms = self.underlyingForms)

    def __unicode__(self):
        return u"\n".join([ u"rule: %s"%r for r in self.rules ] +
                         [self.showMorphology()] +
                         ([u"underlying form: %s ; surfaces = %s"%(u, u" ~ ".join(map(unicode,ss)))
                           for ss,u in self.underlyingForms.iteritems() ]))
    def __str__(self): return unicode(self).encode('utf-8')

    def __eq__(self, o):
        return tuple(self.prefixes + self.suffixes + self.rules) == tuple(o.prefixes + o.suffixes + o.rules) and \
            tuple(self.underlyingForms.iteritems()) == tuple(o.underlyingForms.iteritems())
    def __ne__(self,o): return not (self == o)
    def __hash__(self):
        return hash((tuple(self.prefixes + self.suffixes + self.rules),tuple(self.underlyingForms.iteritems())))
            

    def showMorphology(self):
        lines = []
        for p,s in zip(self.prefixes, self.suffixes):
            x = u"stem"
            if len(p) > 0: x = u"%s + %s"%(p,x)
            if len(s) > 0: x = u"%s + %s"%(x,s)
            lines.append(x)
        return u"\n".join(lines)

    def pretty(self):
        p = u''
        for prefix, suffix in zip(self.prefixes, self.suffixes):
            if len(prefix) == 0 and len(suffix) == 0: continue
            if len(prefix) > 0: p += u''.join(prefix.phonemes) + u'+'
            p += u'stem'
            if len(suffix) > 0: p += u'+' + u''.join(suffix.phonemes)
            p += u'\n'
        p += u'\n'.join([ r.pretty() for r in self.rules ])
        if p == u'': p = u'surface=underlying'
        if p[-1] == u'\n': p = p[:-1]
        return p

    def cost(self, ug = None):
        return self.modelCost(ug) + sum(len(s) for s in self.underlyingForms.values())

    def modelCost(self, UG = None):
        ruleCost = 0.0
        for r in self.rules:
            if UG == None: ruleCost += r.cost()
            else:
                k1 = UG.ruleLogLikelihood(r)[0]
                k2 = getEmptyFragmentGrammar().ruleLogLikelihood(r)[0]
                k = lse(k1 - math.log(2),k2 - math.log(2))
                # change of logarithm base:
                # 1 unit of cost is about log(20)
                k = -k/math.log(20)
                # print "Cost of",r,k
                ruleCost += k
        return ruleCost + sum([ len(s) for s in (self.prefixes + self.suffixes) ])

    def depth(self): return len(self.rules)

    def withoutStems(self):
        return Solution(rules=self.rules, prefixes=self.prefixes, suffixes=self.suffixes)

    def showMorphologicalAnalysis(self):
        print "Morphological analysis:"
        for i in range(len(self.prefixes)):
            print "Inflection %d:\t"%i,
            print self.prefixes[i],
            print "+ stem +",
            print self.suffixes[i]

    def showRules(self):
        print "Phonological rules:"
        for r in self.rules: print r

    def hasTones(self):
        return any( "highTone" in sophisticatedFeatureMap[p]
                    for m in self.prefixes + self.suffixes
                    for p in m.phonemes )

    def mutate(self,bank):
        # mutate a phoneme
        if random() < 0.3:
            newPrefixes = list(self.prefixes)
            newSuffixes = list(self.suffixes)
            for _ in range(sampleGeometric(0.7) + 1):
                i = choice(range(len(self.prefixes)))
                if choice([True,False]): # mutate a prefix
                    newPrefixes[i] = newPrefixes[i].mutate(bank)
                else:
                    newSuffixes[i] = newSuffixes[i].mutate(bank)
            return Solution(self.rules,newPrefixes,newSuffixes)
                
        # mutate a rule
        if random() < 0.5:
            r = choice(self.rules)
            newRules = [ (r.mutate(bank) if q == r else q) for q in self.rules ]
            return Solution(newRules,self.prefixes,self.suffixes)
        # reorder the rules
        if len(self.rules) > 1 and random() < 0.3:
            i = choice(range(len(self.rules)))
            j = choice([ k for k in range(len(self.rules)) if k != i ])
            newRules = [ self.rules[i if k == j else (j if k == i else k)]
                         for k in range(len(self.rules)) ]
            return Solution(newRules,self.prefixes,self.suffixes)
        # delete a rule
        if len(self.rules) > 1 and random() < 0.3:
            newRules = randomlyRemoveOne(self.rules)
            return Solution(newRules,self.prefixes,self.suffixes)
        # insert a rule
        newRules = list(self.rules)
        newRules.insert(choice(range(len(self.rules)+1)), EMPTYRULE.mutate(bank).mutate(bank).mutate(bank).mutate(bank))
        return Solution(newRules,self.prefixes,self.suffixes)
        

    def withoutUselessRules(self):
        return Solution(prefixes = self.prefixes,
                        suffixes = self.suffixes,
                        underlyingForms = self.underlyingForms,
                        rules = [ r for r in self.rules
                                  if len(self.rules) == 1 or (not r.doesNothing()) ])

    
    def transduceUnderlyingForm(self, bank, surfaces, getTrace = False):
        '''surfaces: list of morphs'''
        bound = max([len(s) for s in surfaces if s != None]) + 3
        Model.Global()
        rules = [r.makeDefinition(bank) for r in self.rules ]
        prefixes = [p.makeConstant(bank) for p in self.prefixes ]
        suffixes = [p.makeConstant(bank) for p in self.suffixes ]
        stem = Morph.sample()
        
        countingProblem = len(surfaces) == 3 and tuple(surfaces) == (Morph(u"ǰu"),None,None)
        if countingProblem:
            condition(wordEqual(stem, prefixes[1]))
            condition(wordEqual(stem, suffixes[2]))
        
        traces = []
        for s,prefix, suffix in zip(surfaces,prefixes, suffixes):
            if s != None:
                ur = concatenate3(prefix,stem,suffix)
                condition(wordEqual(s.makeConstant(bank),
                                    applyRules(rules,ur, wordLength(prefix) + wordLength(stem), bound)))
                if getTrace:
                    trace = [ Morph.sample() for j in range(len(rules)) ]
                    for j,t in enumerate(trace):
                        condition(wordEqual(t, applyRules(rules[:j], ur,
                                                          wordLength(prefix) + wordLength(stem),bound)))
                    traces.append(trace)
            elif getTrace: traces.append(None)
        minimize(wordLength(stem))

        try: output = solveSketch(bank,bound,bound)
        except SynthesisFailure: return None

        if not getTrace: return Morph.parse(bank,output,stem)

        traces = [ [ Morph.parse(bank, output, t) for t in trace ] + [surfaces[j]] if trace != None else None
                   for j,trace in enumerate(traces) ]
        return Morph.parse(bank,output,stem),traces

    def _transduceManyStems(self, bank, data):
        
        bound = max([len(s) for surfaces in data for s in surfaces if s != None]) + 3
        
        Model.Global()
        rules = [r.makeDefinition(bank) for r in self.rules ]
        prefixes = [p.makeConstant(bank) for p in self.prefixes ]
        suffixes = [p.makeConstant(bank) for p in self.suffixes ]
        stems = [ Morph.sample() for _ in data ]
        for surfaces, stem in zip(data, stems):
            countingProblem = tuple(surfaces) == (Morph(u"ǰu"),None,None)
            if countingProblem:
                condition(wordEqual(stem, prefixes[1]))
                condition(wordEqual(stem, suffixes[2]))

            minimize(wordLength(stem))
            haveMainCondition = False
            for s,prefix, suffix in zip(surfaces,prefixes, suffixes):
                if s != None:
                    ur = concatenate3(prefix,stem,suffix)
                    predicate = wordEqual(s.makeConstant(bank),
                                          applyRules(rules,ur, wordLength(prefix) + wordLength(stem), bound))
                    if haveMainCondition: auxiliaryCondition(predicate)                        
                    else:
                        condition(predicate)
                        haveMainCondition = True
                        

        try: output = solveSketch(bank,bound,bound)
        except SynthesisFailure:
            assert len(data) == 1,"transduction failed with batch size greater than one"
            return None
        return {surfaces: Morph.parse(bank, output, stem)
                for surfaces, stem in zip(data, stems) }

    def transduceManyStems(self, bank, data, batchSize = None):
        if batchSize is None: batchSize = len(data)

        stems = {}
        completed = 0
        while completed < len(data):
            b = data[completed:completed+batchSize]
            stems.update(self._transduceManyStems(bank, b) or {})
            completed += batchSize        

        return Solution(rules = self.rules,
                        prefixes = self.prefixes,
                        suffixes = self.suffixes,
                        underlyingForms = stems)
