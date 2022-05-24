# -*- coding: utf-8 -*-
from features import *
from morph import *

import os

phoneme2speechSymbol = {
    u'p':'p',
    u'b':'b',
    u'd':'d',
    u't':'t',
    u"č": 'tS',
    u"ǰ": 'dZ',
    u'k': 'k',
    u'g': 'g',
    u"θ": 'T',
    u"ð": 'D',
    u's': 's',
    u'z': 'z',
    u"š": 'S',
    u"ž": 'Z',
    u"h": "h",
    u"m": "m",
    u"n": "n",
    u"ŋ": "N",
    u"l": "l",
    u"r": "r",
    u"y": 'j',
    u"w": "w",
    u'f': 'f',
    u'v': 'v',

    u"ə": '@',
    u"ɛ": 'E',
    u"a": '0',
    u"ɩ": 'I',
    u'i': 'i',
    u'e': 'eI',
    u'o': 'oU',
    u'æ': 'aa',
    u'u': 'u:',
}

def speakMorph(m):
    symbolSequence = "".join(phoneme2speechSymbol[p] for p in m.phonemes)
    os.system("espeak  -s 120 [[%s]]"%symbolSequence)
def translateToSpeechSymbols(phonemes):
    return "".join(phoneme2speechSymbol[p] for p in tokenize(phonemes) )
def speakMatrix(p,saveTo = None):
    toSpeak = []
    for inflections in p:
        try:
            toSpeak.append('[[' + " ".join(map(translateToSpeechSymbols,inflections)) + ']]')
        except KeyError as ex:
            print "Skipping something due to missing a key",ex
    if saveTo == None: saveTo = ""
    else: saveTo = " -w %s"%saveTo
    os.system("espeak -ven-us %s -s 120  -g 30 -x  -l 3000 \"%s\""%(saveTo,"\n".join(toSpeak)))
#            speakMorph(Morph(tokenize(x)))

if __name__ == "__main__":
    from problems import *
    speakMatrix(interactingProblems[1].data,"stimuli/Polish.wav")
    speakMatrix(underlyingProblems[10].data,"stimuli/Russian.wav")
    speakMatrix(underlyingProblems[9].data,"stimuli/Samoan.wav")
    speakMatrix(underlyingProblems[11].data,"stimuli/English.wav")
    speakMatrix([(u"fefeda",),
                 (u"gogotu",),
                 (u"dadati",),
                 (u"ðɛðɛwo",),
                 (u"mamane",)],
                "stimuli/AAB.wav")
    
