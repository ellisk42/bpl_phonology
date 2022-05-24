# -*- coding: utf-8 -*-

from result import *
from compileRuleToSketch import compileRuleToSketch
from utilities import *
from solution import *
from features import FeatureBank, tokenize
from rule import * # Rule,Guard,FeatureMatrix,EMPTYRULE
from morph import Morph,observeWord
from sketchSyntax import Expression,makeSketchSkeleton
from sketch import *
from supervised import SupervisedProblem
from textbook_problems import *
from latex import latexMatrix

from pathos.multiprocessing import ProcessingPool as Pool
import random
import sys
import pickle
import math
from time import time
import itertools
import copy

data = [('ap', 'aba'), ('at', 'ada'), ('ab', 'aba'), ('ad', 'ada')] # duples corresponding to slots of a paradigm

# Introduce a new global model and also construct a feature bank (inventory of features and phonemes) behind the scenes
globalModel([w for ws in data for w in ws ])

prefix = Morph.sample()
suffix = Morph.sample()
rule = Rule.sample()

stems = [Morph.sample() for i in range(4)]


new_data = zip(stems, data) # generates a list of tuples with each ith element corresponding to a tuple at position i in each list

for stem, (surface1, surface2) in new_data:
        maximumLength = max(len(surface1), len(surface2)) + 1
	predicted_surface1 = applyRule(rule, stem, maximumLength) # first number specifies for morpheme boundaries (length of string until suffix (len(prefix + stem))); second number is bounded amount that rule can look at when applying rule (should be bigger than the longest stem)
	predicted_surface2 = applyRule(rule, concatenate(concatenate(prefix, stem), suffix), maximumLength) # first number specifies for morpheme boundaries (length of string until suffix (len(prefix + stem))); second number is bounded amount that rule can look at when applying rule (should be bigger than the longest stem)
        observeWord(surface1, predicted_surface1)
        observeWord(surface2, predicted_surface2)

minimize(ruleCost(rule) + wordLength(prefix) + sum(wordLength(stem) for stem in stems) + wordLength(suffix))
# vs. having minimize(wordLength(prefix) + sum(wordLength(stem) for stem in stems) + wordLength(suffix)) and minimize(ruleCost(rule)) --> picks out a point in Pareto Frontier where you can't make lexicon smaller without increasing rules and vice versa
output = solveSketch(None, unroll=10, maximumMorphLength=10)
if output is not None:
        print "successfully resolved constraints"
        print(Morph.parse(prefix))
        print(Morph.parse(suffix))
        print([Morph.parse(stem) for stem in stems])
        print(Rule.parse(rule))
else:
        print "could not successfully solve constraints"
