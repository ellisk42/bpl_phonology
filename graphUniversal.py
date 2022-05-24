# -*- coding: utf-8 -*-

from utilities import *
from fragmentGrammar import *

import sys


fn = sys.argv[1]
ug = FragmentGrammar.load(fn)

names = []
likelihoods = []

for t,w,f in ug.fragments:
    f = unicode(f)
    t = t.__name__
    if u'[' in f:
        correspondence = [(u'Guard', u'Trigger'),
                          (u'BoundarySpecification', u'+'),
                          (u'OffsetSpecification', u'ℤ'),
                          (u'PlaceSpecification', u'αplace'),
                          (u'Specification', u'PhonemeSet'),
                          (u'ConstantPhoneme', u'Phoneme')]
        for k,v in correspondence:
            f = f.replace(k,v)
        f = f.replace(u"FeatureMatrix",u"FM").replace(u"PhonemeSet",u"FM").replace("FC","FM")
        f = f.replace(u" ---> ",u"→")
        f = f.replace(u" [","[").replace(u" ]","]").replace(u"[ ",u"[").replace(" / ","/").replace(" _ ","_").replace(" /","/").replace(" _","_").replace("] ","]").replace(u"*",u"₀")
        for original, shortened in featureAbbreviation.iteritems():
            f = f.replace(unicode(original),unicode(shortened))

        t = t.replace("Guard","Trigger").replace("Specification","FM")
        name = t + "::=" + f
        names.append(name)
        likelihoods.append(w)
        print w,name

