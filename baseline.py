# -*- coding: utf-8 -*-
import sys

from textbook_problems import *
from morph import *


diacritics = {
    u"^h": u"ʰ",
    u"^y": u"ʲ",
    u":": u"ː",
}

convertToIPA = {
    u"n̆": u"ɳ",
    u"x̯": u"ç",
    u"φ|": u"ɸ",
    u"β|": u"β",
    # unrounded vowels
    # u"i": [voice,tense,high],
    # u"ɨ": [voice,tense,high,back],
    u"ɩ": u"ɪ",
#    u"e": [voice,tense],
#    u"ə": [voice,back],
    # u"ɛ": [voice,low], # TODO: is this actually +low? halle seems to think so!
    # u"æ": [voice,low,tense],
#    u"a": [voice,low,tense,back],
#    u"ʌ": [voice,back,tense],
    # rounded vowels
#    u"u": [voice,tense,high,back,rounded],
    u"ü": u"y",#[voice,tense,high,rounded],
#    u"ʊ": [voice,high, back, rounded],
#    u"o": [low,voice,tense,back,rounded],
    u"ö": u"ø",#[voice,tense,rounded],
#    u"ɔ": [voice,back,rounded],
    #possibly missing are umlauts

    # consonance
#    u"p": [anterior,],
#    u"p^y": u"pʲ",
#    u"p̚": [anterior,unreleased],
#    u"p^h": u"pʰ",#[anterior,aspirated],
#    u"b": [anterior,voice],
    # u"b^h": [anterior,voice, aspirated],
    # u"f": [anterior,continuant],
    # u"v": [anterior,continuant,voice],
    # u"β": [anterior,continuant,voice],
    # u"m": [anterior,nasal,voice,sonorant],#continuant],
#    u"m̩": [anterior,nasal,voice,sonorant,syllabic],
#    u"m̥": [anterior,nasal,sonorant],#,continuant],
#    u"θ": [anterior,continuant,coronal],
#    u"d": [anterior,voice,coronal],
    #u"d̪": [voice,coronal],
    u"d^z": u"ʣ",#[anterior,coronal,voice,delayedRelease],

    u"ř": u"ɾ",
#    u"t": [anterior,coronal],
    #u"t̪": [coronal],
#    u"t̚": [anterior,coronal,unreleased],
    u"t^s": u"ʦ",#[anterior,coronal,delayedRelease],
#    u"t^h": [anterior,aspirated,coronal],
#    u"ṭ": [anterior,retroflex,coronal],
#    u"ḍ": [anterior,retroflex,coronal,voice],
#    u"ṛ": [anterior,retroflex,coronal,voice,continuant],
#    u"ð": [anterior,continuant,voice,coronal],
#    u"z": [anterior,continuant,voice,coronal, sibilant],
    u"ǰ": u"ʤ",#[voice,coronal,sibilant],#alveopalatal,
    u"ž": u"ʒ",#[continuant,voice,coronal, sibilant],#alveopalatal,
#    u"ž^y": [continuant,voice,coronal, sibilant, palletized],#alveopalatal,
#    u"s": [anterior,continuant,coronal, sibilant],
#    u"ṣ": [anterior,continuant,coronal, sibilant, retroflex],
    u"ṣ": u"ṣ",
    # u"n": [anterior,nasal,voice,coronal,sonorant],#continuant],
    # u"n̩":  [anterior,nasal,voice,coronal,syllabic,sonorant],
    # u"ṇ": [anterior,retroflex,nasal,voice,sonorant],#continuant],
    # u"n̥": [anterior,nasal,coronal,sonorant],#continuant],

    # conjecture: these are the same
    # u"ñ": [nasal,voice,coronal,sonorant],
    # u"n̆": [nasal,voice,coronal,sonorant],

    # u"ɲ": [nasal,voice,coronal,sonorant,high],
    # u"ɲ̩": [nasal,voice,coronal,sonorant,high,syllabic],
    
    u"š": u"ʃ",#[continuant,coronal, sibilant],#alveopalatal,
#    u"c": [palatal,coronal], # NOT the same thing as palletized
#    u"ç": [continuant,palatal],
    u"ɉ": u"ɟ",
    u"l`": "l2",
#    u"x̯": [palatal,coronal,continuant],
    u"č": u"ʧ",#c[coronal,sibilant],#alveopalatal,
#    u"č^h": [coronal,sibilant,aspirated],#alveopalatal,
#    u"k": [back,high],
#   u"k̚": [back,high,unreleased],
    # u"k^h": [back,high,aspirated],
    # u"k^y": [back,high,palletized],
#    u"x": [back,high,continuant],
    u"X": u"χ",#[back,continuant], # χ
#    u"x^y": [back,high,continuant,palletized],
    u"g": u"ɡ",#[back,high,voice],
    # u"g^h": [back,high,voice,aspirated],
    # u"g^y": [back,high,voice,palletized],
#    u"ɣ": [back,high,continuant,voice],
    # u"ŋ": [back,high,nasal,voice,sonorant],#continuant],
    # u"ŋ̩":  [back,high,nasal,voice,sonorant,syllabic],
#    u"q": [back],
    u"N": u"ɴ",#[back,nasal,voice],#continuant],
    u"G": u"ɢ",#[back,voice],
#    u"ʔ": [sonorant,low],#laryngeal,
#    u"h": [continuant,sonorant,low],#laryngeal,
#    u"ħ": [back, low,continuant,sonorant],

    # glides
    # u"w": [glide,voice,sonorant,continuant],
    # u"w̥": [glide,sonorant,continuant],
    u"y": u"j",#[glide,palletized,voice,sonorant,continuant],
#    u"j": [glide,palletized,voice,sonorant,continuant],

    # liquids
#    u"r": [liquid,voice,coronal,sonorant,continuant],
    # u"r̃": [liquid,trill,voice,coronal,sonorant,continuant],
    # u"r̥̃": [liquid,trill,coronal,sonorant,continuant],
    # u"ř": [liquid,flap,voice,coronal,sonorant,continuant],
#    u"l": [liquid,lateral,voice,coronal,sonorant,continuant],
    # u"l`": [liquid,secondStress,lateral,voice,coronal,sonorant,continuant],
    # u"l̥": [liquid,lateral,coronal,sonorant,continuant],
    # u"ʎ": [liquid,lateral,voice,palatal,sonorant,continuant],
    # u"ł": [liquid,lateral,voice,back,high,sonorant,continuant],
#    u"̌l": [liquid,lateral,voice,coronal,sonorant],

    # I'm not sure what this is
    # I think it is a mistranscription, as it is in IPA but not APA
    # u"ɲ": []
}

def convertToBaseline(x):
    print(x)
    x = Morph(x)
    phonemes = []
    for p in x.phonemes:
        prefix = p
        suffix = u""
        while any( prefix.endswith(d) for d in diacritics ):
            d = [d for d in diacritics if prefix.endswith(d) ][0]
            prefix = prefix.replace(d,u"")
            suffix = suffix + diacritics[d]
        phonemes.append(convertToIPA.get(prefix, prefix) + suffix)
    return u"".join(phonemes)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument("problems",type=str,nargs='+')
    arguments = parser.parse_args()

    for problem in arguments.problems:
        problemName = problem
        try:
            problem = Problem.named[problem]
        except:
            print("Could not find problem %s"%problem)
            sys.exit(0)

        if problem.parameters and problem.parameters.get("type",None) == "alternation":
            alternation = problem.parameters["alternations"]
            message = u"\n".join([convertToBaseline(x) for x in problem.data ] + \
                                 [u"U," + convertToBaseline(u) + u"," + convertToBaseline(v)
                                  for u,v in alternation[0].iteritems() ])
        else:
            def mayTheFourthBeWithYou(zz):
                if len(zz) >= 4 or True: return zz
                return list(zz) + [None]*(4 - len(zz))
            message = u"\n".join(u",".join(convertToBaseline(x) if x is not None else u""
                                           for x in mayTheFourthBeWithYou(xs))
                                 for xs in problem.data)
        print "Problem",problemName
        print message
        with open("CSV/%s.csv"%problemName,"w") as handle:
            handle.write(message.encode('utf8'))
