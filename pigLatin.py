# -*- coding: utf-8 -*-

from utilities import *

from supervised import SupervisedProblem
from features import FeatureBank, tokenize
from rule import Rule
from morph import Morph
from sketch import *

'''
Pig Latin rules:
1. Copy the first consonant to the end:
   # > 1 / # C_1 [ ]* _ 
2. Delete the first consonant:
   C ---> Ø / # _ 
3. Append e:
   # > e / _
'''

data = {}
# learn to delete the first character
data['Latin1'] = [(u"pɩg", u"ɩg"),#pe"),
                    (u"latɩn", u"atɩn"),#le"),
                    (u"no", u"o"),#ne"),
                    # (u"it", u"ite"),
                    # (u"ask", u"ask")
]
# learn to append "e"
data['Latin2'] = [(u"pɩg", u"pɩge"),#pe"),
                    (u"latɩn", u"latɩne"),#le"),
                    (u"no", u"noe"),#ne"),
                    (u"it", u"ite"),
                     (u"ask", u"aske")
]
# learn to copy the first letter only if it is a consonant
data['Latin3'] = [(u"pɩg", u"pɩgp"),#pe"),
                    (u"latɩn", u"latɩnl"),#le"),
                    (u"no", u"non"),#ne"),
                    (u"it", u"it"),
                     (u"ask", u"ask")
]
# learn pig Latin. System produces:
# Ø ---> -2 / # [ -vowel ] [  ]* _ #
# [ -vowel ] ---> Ø / # _ 
# Ø ---> e /  _ #
data['Latin'] = [(u"pɩg", u"ɩgpe"),#pe"),
      (u"latɩn", u"atɩnle"),#le"),
      (u"no", u"one"),#ne"),
      (u"it", u"ite"),
      (u"ask", u"aske")
]

# Ø ---> 1 /  _ σ
# Ø ---> d /  _ #
# Ø ---> ə /  _ #
data['Chinese'] = [(u"xaw",u"xawxawdə"),
                   (u"man",u"manmandə"),
#                   (u"kwaj",u"kwajkwajdə"),
#                   (u"çin",u"çinçində"),
                   (u"le",u"leledə")]



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "Learn pig Latin and Chinese")
    parser.add_argument('task',
                        choices = ["Chinese","Latin","Latin1","Latin2","Latin3"],
                        default = "Latin")
    parser.add_argument("-d","--depth",default = 1,type = int)
    arguments = parser.parse_args()

    examples = data[arguments.task]
    depth = arguments.depth

    leaveSketchOutput()
    solution = SupervisedProblem([ (Morph(tokenize(x)), Constant(0), Morph(tokenize(y))) for x,y in examples ],
                                 syllables = True).solve(depth)
    
    if solution == None:
        print "No solution."
    else:
        for r in solution: print r
