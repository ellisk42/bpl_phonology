# -*- coding: utf-8 -*-

from solution import Solution
from morph import Morph

import re
from features import *
from rule import *

'''
Why is there no good parser combinator library for Python...
A parser is a function from strings to a stream of tuples of (unconsumed suffix, value)
'''

def eatWhiteSpace(s):
    j = 0
    while j < len(s) and s[j].isspace(): j += 1
    yield (s[j:],None)
def constantParser(k,v = None):
    def p(s):
        if s.startswith(k):
            yield (s[len(k):],v)
    return p
def whitespaceDelimited(p):
    return concatenate(eatWhiteSpace,p,eatWhiteSpace,
                       combiner = lambda v1,v2,v3: v2)

defaultCombiner = lambda *vs: tuple(vs)
def concatenate2(p,q,combiner = defaultCombiner):
    def newParser(s):
        for suffix, first in p(s):
            for newSuffix, second in q(suffix):
                yield (newSuffix, combiner(first, second))
    return newParser

def concatenate(*components, **keywords):
    combiner = keywords.get("combiner",defaultCombiner)
    if len(components) < 2: raise Exception('concatenate: not enough components')
    if len(components) == 2: return concatenate2(components[0],components[1],combiner = combiner)
    suffixParser = concatenate(*components[1:])
    def recursiveCombiner(hd,tl):
        #print "concatenate_%d combiner called with %s\t%s"%(len(components),hd,tl)
        fullArguments = [hd] + list(tl)
        #print "\tfullArguments",fullArguments
        return combiner(*fullArguments)
    return concatenate2(components[0], suffixParser,
                        combiner = recursiveCombiner)
        

def alternation(*alternatives):
    def newParser(s):
        for a in alternatives:
            for x in a(s): yield x
    return newParser

def repeat(p):
    def newParser(s):
        generator = p(s)
        haveYieldedSomething = False

        while True:
            try:
                (suffix, value) = generator.next()
                for finalSuffix,values in newParser(suffix):
                    yield (finalSuffix,[value] + values)                
                    haveYieldedSomething = True
            except StopIteration:
                if not haveYieldedSomething: yield (s,[])
                break
            
    return newParser

def mapParserOutput(p,f):
    def newParser(s):
        for suffix, value in p(s): yield (suffix,f(value))
    return newParser

def optional(p):
    return alternation(constantParser(""), p)


def whitespaceDelimitedSequence(*things):
    things = map(whitespaceDelimited,things)
    return concatenate(*things)

def runParser(p,s):
    for suffix, result in p(s):
        if len(suffix) == 0: return result
    return None

featureParser = alternation(*[ constantParser(p + f, (p == '+',f)) 
                               for f in set([ f for fs in sophisticatedFeatureMap.values() for f in fs ] + \
                                            [ f for fs in simpleFeatureMap.values() for f in fs ])
                                for p in ['-','+'] ])
whitespaceFeatureParser = whitespaceDelimited(featureParser)
featuresParser = repeat(whitespaceFeatureParser)
matrixParser = concatenate(constantParser('['),
                           whitespaceDelimited(featuresParser),
                           constantParser(']'),
                           combiner = lambda l,fp,r: FeatureMatrix(fp))
phonemeParser = alternation(*[ constantParser(k,ConstantPhoneme(k)) for k in featureMap
                               if k != '*'])
placeParser = alternation(constantParser('place+1', PlaceSpecification(1)),
                          constantParser('place-1', PlaceSpecification(-1)))
consonantParser = constantParser('C',FeatureMatrix([(False,'vowel')]))
vowelParser = constantParser('V',FeatureMatrix([(True,'vowel')]))
boundaryParser = constantParser('+',BoundarySpecification())
specificationParser = alternation(matrixParser,phonemeParser,boundaryParser,vowelParser,consonantParser,placeParser)

optionalEndOfStringParser = concatenate(constantParser("{#,",None),
                                        specificationParser,
                                        constantParser("}",None),
                                        combiner = lambda _1,spec,_2: ("{#,",spec))

# yields ()
guardSpecificationParser = concatenate(alternation(specificationParser,optionalEndOfStringParser),
                                       optional(whitespaceDelimited(constantParser('*','*'))))
                               
nullParser = alternation(constantParser("0",EmptySpecification()),
                         constantParser(u"Ø",EmptySpecification()))

focusChangeParser = alternation(*([ constantParser(str(n),OffsetSpecification(n)) for n in [-2,-1,1,2] ] + [specificationParser,nullParser]))

rightGuardParser = whitespaceDelimitedSequence(repeat(whitespaceDelimited(guardSpecificationParser)),
                                               optional(constantParser('#','#')))
leftGuardParser = whitespaceDelimitedSequence(optional(constantParser('#','#')),
                                              repeat(whitespaceDelimited(guardSpecificationParser)))

arrowParser = alternation(concatenate(repeat(constantParser('-')),constantParser('>')),
                          constantParser(u'⟶'))
ruleParser = whitespaceDelimitedSequence(focusChangeParser,
                                         arrowParser,
                                         focusChangeParser,
                                         constantParser('/'),
                                         leftGuardParser,
                                         constantParser('_'),
                                         rightGuardParser)

def parseRule(s):
    # if u'+stop' in s:
    #     # This is shorthand
    #     s = s.replace(u'+stop',u'-sonorant -continuant')
    p = runParser(ruleParser,s)
    if p == None: return None
    [focus,_,change,_,(le,ls),_,(rs,re)] = p

    def unpackOptionalEndOfString(mayBeEndOfString):
        if isinstance(mayBeEndOfString,tuple) and mayBeEndOfString[0] == "{#,":
            return mayBeEndOfString[1]
        return mayBeEndOfString
    def hasOptionalEnding(mayBeEndOfString):
        return isinstance(mayBeEndOfString,tuple) and mayBeEndOfString[0] == "{#,"

    l = Guard(endOfString = '#' == le,
              optionalEnding = any([ hasOptionalEnding(s) for s,_ in ls ]),
              specifications = reversed([ unpackOptionalEndOfString(s) for s,_ in ls ]),
              starred = any([ s == '*' for _,s in ls ]),
              side = 'L')
    r = Guard(endOfString = '#' == re,
              optionalEnding = any([ hasOptionalEnding(s) for s,_ in rs ]),
              specifications = [unpackOptionalEndOfString(s) for s,_ in rs ],
              starred = any([s == '*' for _,s in rs ]),
              side = 'R')

    return Rule(focus, change, l,r)

def parseSolution(s):
    def removeComment(y):
        if ';' in y: return y[:y.index(';')].strip()
        y = y.strip()
        if len(y) == 0 or y[0] == '#': return ''
        return y
    lines = [ removeComment(x) for x in s.split('\n') ]
    prefixes = []
    suffixes = []
    rules = []
    for l in lines:
        if 'stem' in l:
            [prefix, suffix] = l.split('stem')
            prefix = prefix.replace('+','').strip()
            suffix = suffix.replace('+','').strip()
            prefixes.append(Morph(tokenize(prefix)))
            suffixes.append(Morph(tokenize(suffix)))
        elif len(l) > 0:
            r = parseRule(l)
            if r == None:
                print "Could not parse '%s'"%l
                assert False
            rules.append(r)
    return Solution(rules, prefixes, suffixes)

if __name__ == '__main__':
    print parseRule(u'o > e / a [ ] _ V {#,C}')
    print parseRule('0 > -2 / #[-vowel][]* _ e #').pretty()
    print(parseRule('[ ] > place+1 / _'))
    print parseSolution(u''' + stem + 
 + stem + ə
    [-sonorant] > [-voice] / _ #''')
