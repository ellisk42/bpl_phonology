import math

import random

languages = [u'Turkish', u'Swahili', u'Icelandic', u'Dutch', u'Kikuria', u'Samoan', u'Ewe', u'Palauan', u'Catalan', u'Jita', u'Lhasa Tibetan', u'North Saami', u'Korean', u'Kerewe', u'Yawelmani', u'Indonesian', u'Latin', u'Makonde', u'Hungarian', u'Kikurai', u'Lithuanian', u'Axininca Campa', u'Ganda', u'Bukusu', u'Serbo-Croatian', u'Russian', u'Thai', u'Tibetan', u'Koasati', u'Armenian', u'Mohawk', u'Kikuyu', u'Finnish', u'Yokuts', u'Anxiang', u'English', u'Lardil', u'Japanese', u'Proto-Bantu', u'Modern Greek', u'Kera', u'Somali', u'Osage', u'Tunica', u'Kishambaa', u'Zoque', 'Ukrainian', u'Ancient Greek', u'Gen', u'Amharic', u'German', u'Lumasaaba', u'Papago', u'Quechua', u'Sakha (Yakut)', u'Polish', u'Farsi']

random.shuffle(languages)
languages = languages[:50]

print "\\node[align=center,large](ug) at (0,0) {\\large universal\\\\\\phantom{t }\\\\\\large grammar};"
for n,language in enumerate(languages):
    r = 4
    
    angle = n*6.28/len(languages)
    x = r*math.cos(n*6.28/len(languages))
    y = r*math.sin(angle)
    if 3.14/2 <= angle <= 3.14:
        angle = angle - 3.14
    elif 3.14 <= angle <= 3.14 + 3.14/2:
        angle = angle - 3.14
    print """
\\node[rotate=%s](this) at (%s,%s) {\\large %s};
\draw[->] (ug) -- (this);
"""%(angle*360/6.28,x,y,language)
