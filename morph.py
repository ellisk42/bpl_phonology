# -*- coding: utf-8 -*-

from sketchSyntax import define, FunctionCall, getGeneratorDefinition, globalConstant, And, Or, Constant,condition, Not
from sketch import makeConstantWord, getGeneratorDefinition, indexWord, wordLength, wordEqual, getLastOutput
from features import FeatureBank,featureMap,tokenize
from utilities import *

from random import choice
import re

class Morph():
    def __init__(self, phonemes):
        if isinstance(phonemes,unicode): phonemes = tokenize(phonemes)
        self.phonemes = phonemes
    def __unicode__(self):
        return u"/{}/".format(u"".join(self.phonemes))
    def __str__(self): return unicode(self).encode('utf-8')
    def __repr__(self): return str(self)
    # this interferes with parallel computation - probably because it messes up serialization
    # def __repr__(self): return unicode(self)
    def __len__(self): return len(self.phonemes)
    def __add__(self, other): return Morph(self.phonemes + other.phonemes)
    def __eq__(self, other):
        return str(self) == str(other)
    def __hash__(self): return hash(tuple(self.phonemes))
    def __ne__(self, other):
        return str(self) != str(other)
    def __getitem__(self, sl):
        if isinstance(sl,int): return self.phonemes[sl]
        if isinstance(sl,slice):
            return Morph(self.phonemes[sl.start:sl.stop:sl.step])

    def mutate(self,bank):
        # remove a phoneme
        if len(self) > 0 and choice([True,False]):
            return Morph(randomlyRemoveOne(self.phonemes))
        # insert a phoneme
        p = choice(bank.phonemes)
        newPhonemes = list(self.phonemes)
        newPhonemes.insert(choice(range(len(self) + 1)),p)
        return Morph(newPhonemes)

    def patternInstantiations(self):
        if len(self) == 0: yield self
        else:
            if self.phonemes[0] == u'?':
                for suffix in Morph(self.phonemes[1:]).patternInstantiations():
                    yield Morph([u'*'] + suffix.phonemes)
                    yield suffix
            else:
                for suffix in Morph(self.phonemes[1:]).patternInstantiations():
                    yield Morph([self.phonemes[0]] + suffix.phonemes)
    def match(self, bank, variable):
        def singleMatch(m):
            predicate = [wordLength(variable) == len(m)]
            for i,p in enumerate(m.phonemes):
                if p != u'*':
                    predicate.append(indexWord(variable,Constant(i)) == bank.phonemeConstant(p))
            return And(predicate)
        return Or([singleMatch(m) for m in self.patternInstantiations() ])



    @staticmethod
    def sample():
        return define("Word", FunctionCall("unknown_word",[]), globalToHarnesses = True)

    def makeConstant(self, bank):
        return makeConstantWord(bank, "".join(self.phonemes))

    # Returns a variable that refers to a sketch object
    def makeDefinition(self, bank):
        return globalConstant("Word", self.makeConstant(bank))


    @staticmethod
    def parse(*arguments):
        if len(arguments) == 3:
            bank, output, variable = tuple(arguments)
        elif len(arguments) == 2:
            output, variable = tuple(arguments)
            bank = FeatureBank.ACTIVE
        elif len(arguments) == 1:
            variable = arguments[0]
            bank = FeatureBank.ACTIVE
            output = getLastOutput()
        if variable.definingFunction != None:
            # Search for the global definition, get the unique variable name it corresponds to, and parse that
            variable, output = getGeneratorDefinition(variable.definingFunction, output)
            return Morph.parse(bank, output, variable)

        pattern = 'Word.* %s.* = new Word\(l=([0-9]+), s=([0-9a-zA-Z_]+)\);'%variable
        m = re.search(pattern, output)
        if not m: raise Exception('Could not find word %s in:\n%s'%(variable,output))

        l = int(m.group(1))
        s = m.group(2)
        phones = []
        for p in range(l):
            pattern = '%s\[%d\] = phoneme_([0-9]+)_'%(s,p)
            m = re.search(pattern, output)
            if not m:
                print output
                print pattern
                raise Exception('Could not find %dth phoneme of %s'%(p,variable))
            phones.append(bank.phonemes[int(m.group(1))])
        return Morph(phones)

def observeWord(surface, predicted, bank=None):
    """adds an extra condition that the prediction must be equal to the surface form"""
    bank = bank or FeatureBank.ACTIVE
    if not isinstance(surface,Morph):
        surface = Morph(surface)
    condition(wordEqual(predicted, Morph.makeConstant(surface, bank)))

def observeWordIfNotMemorized(surface, predicted, flip, bank=None):
    """adds an extra condition that the prediction must be equal to the surface form"""
    bank = bank or FeatureBank.ACTIVE
    if not isinstance(surface,Morph):
        surface = Morph(surface)
    condition( flip == Not(wordEqual(predicted, Morph.makeConstant(surface, bank))) )
