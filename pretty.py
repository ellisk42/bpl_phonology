from rule import *
from latex import *
from parseSPE import *


import sys
import codecs
f = codecs.open(sys.argv[1],encoding='utf-8')

for l in f:
    if len(l.strip()) == 0:
        print l
        continue

    
    r = parseRule(l)
    print r.latex()

    
