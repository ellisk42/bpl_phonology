# -*- coding: utf-8 -*-

secondStress = "secondStress"
palatal = "palatal"
palletized = "palletized"
sibilant = "sibilant"
sonorant = "sonorant"
coronal = "coronal"
retroflex = "retroflex"
creaky = "creaky"
risingTone = "risingTone"
highTone = "highTone"
lowTone = "lowTone"
middleTone = "middleTone"
longVowel = "long"
vowel = "vowel"
tense = "tense"
lax = "lax"
high = "high"
middle = "middle"
low = "low"
front = "front"
central = "central"
back = "back"
rounded = "rounded"
bilabial = "bilabial"
stop = "stop"
voice = "voice"
fricative = "fricative"
labiodental = "labiodental"
dental = "dental"
alveolar = "alveolar"
#labiovelar = "labiovelar"
velar = "velar"
nasal = "nasal"
uvular = "uvular"
glide = "glide"
liquid = "liquid"
lateral = "lateral"
trill = "trill"
flap = "flap"
affricate = "affricate"
alveopalatal = "alveopalatal"
anterior = "anterior"
aspirated = "aspirated"
unreleased = "unreleased"
laryngeal = "laryngeal"
pharyngeal = "pharyngeal"
syllableBoundary = "syllableBoundary"
wordBoundary = "wordBoundary"
continuant = "continuant"
syllabic = "syllabic"
delayedRelease = "delayedRelease"

# Not actually features...
wildFeature = "wild"
optionalFeature = "optional"

featureAbbreviation = {
palatal:"palatal",
palletized:"pal",
sibilant:"sib",
sonorant:"son",
coronal:"cor",
retroflex:"retro",
creaky:"creaky",
risingTone:"riseTn",
highTone:"hiTn",
lowTone:"loTn",
middleTone:"midTn",
longVowel:"long",
vowel:"vowel",
tense:"tense",
lax:"lax",
high:"hi",
middle:"mid",
low:"lo",
front:"front",
central:"central",
back:"bk",
rounded:"rnd",
bilabial:"bilabial",
stop:"stop",
voice:"voice",
fricative:"fricative",
labiodental:"labiodental",
dental:"dental",
alveolar:"alveolar",
#labiovelar:"labiovelar",
velar:"velar",
nasal:"nasal",
uvular:"uvular",
glide:"glide",
liquid:"liq",
lateral:"lat",
trill:"trill",
flap:"flap",
affricate:"affricate",
alveopalatal:"alveopalatal",
anterior:"ant",
aspirated:"asp",
unreleased:"unreleased",
laryngeal:"laryngeal",
pharyngeal:"pharyngeal",
continuant:"cont",
syllabic:"syl",
delayedRelease:"delRelease"
}

sophisticatedFeatureMap = {
    u"*": [wildFeature],
    u"?": [optionalFeature],
    
    # unrounded vowels
    u"i": [voice,tense,high],
    u"ɨ": [voice,tense,high,back],
    u"ɩ": [voice,high],
    u"e": [voice,tense],
    u"ə": [voice,back],
    u"ɛ": [voice,low], # TODO: is this actually +low? halle seems to think so!
    u"æ": [voice,low,tense],
    u"a": [voice,low,tense,back],
    u"ʌ": [voice,back,tense],
    # rounded vowels
    u"u": [voice,tense,high,back,rounded],
    u"ü": [voice,tense,high,rounded],
    u"ʊ": [voice,high, back, rounded],
    u"o": [voice,tense,back,rounded],
    u"ö": [voice,tense,rounded],
    u"ɔ": [voice,back,rounded],
    #possibly missing are umlauts

    # consonance
    u"p": [anterior,],
    u"p^y": [anterior,palletized],
    u"p̚": [anterior,unreleased],
    u"p^h": [anterior,aspirated],
    u"b": [anterior,voice],
    u"b^h": [anterior,voice, aspirated],
    u"f": [anterior,continuant],
    u"φ": [anterior,continuant],
    u"φ|": [anterior,continuant,bilabial],
    u"f^y": [anterior,continuant,palletized],
    u"v": [anterior,continuant,voice],
    u"β": [anterior,continuant,voice],
    u"β|": [anterior,continuant,voice,bilabial],
    u"m": [anterior,nasal,voice,sonorant],#continuant],
    u"m̩": [anterior,nasal,voice,sonorant,syllabic],
    u"m̥": [anterior,nasal,sonorant],#,continuant],
    u"θ": [anterior,continuant,coronal],
    u"d": [anterior,voice,coronal],
    #u"d̪": [voice,coronal],
    u"d^z": [anterior,coronal,voice,delayedRelease],
    u"d^z^h": [anterior,coronal,voice,delayedRelease,aspirated],
    u"t": [anterior,coronal],
    #u"t̪": [coronal],
    u"t̚": [anterior,coronal,unreleased],
    u"t^s": [anterior,coronal,delayedRelease],
    u"t^h": [anterior,aspirated,coronal],
    u"ṭ": [anterior,retroflex,coronal],
    u"ḍ": [anterior,retroflex,coronal,voice],
    u"ṛ": [anterior,retroflex,coronal,voice,continuant],
    u"ð": [anterior,continuant,voice,coronal],
    u"z": [anterior,continuant,voice,coronal, sibilant],
    u"ǰ": [voice,coronal,sibilant],#alveopalatal,
    u"ž": [continuant,voice,coronal, sibilant],#alveopalatal,
    u"ž^y": [continuant,voice,coronal, sibilant, palletized],#alveopalatal,
    u"s": [anterior,continuant,coronal, sibilant],
    u"ṣ": [anterior,continuant,coronal, sibilant, retroflex],
    u"n": [anterior,nasal,voice,coronal,sonorant],#continuant],
    u"n̩":  [anterior,nasal,voice,coronal,syllabic,sonorant],
    u"ṇ": [anterior,retroflex,nasal,voice,sonorant],#continuant],
    u"n̥": [anterior,nasal,coronal,sonorant],#continuant],

    # conjecture: these are the same
    u"ñ": [nasal,voice,coronal,sonorant],
    u"n̆": [nasal,voice,coronal,sonorant],

    u"ɲ": [nasal,voice,coronal,sonorant,high],
    u"ɲ̩": [nasal,voice,coronal,sonorant,high,syllabic],
    
    u"š": [continuant,coronal, sibilant],#alveopalatal,
    u"c": [palatal,coronal], # NOT the same thing as palletized
    u"ç": [continuant,palatal],
    u"ɉ": [voice,palatal],
    u"x̯": [palatal,coronal,continuant],
    u"č": [coronal,sibilant],#alveopalatal,
    u"č^y": [coronal,sibilant,palletized],#alveopalatal,
    u"č^h": [coronal,sibilant,aspirated],#alveopalatal,
    u"k": [back,high],
    u"k̚": [back,high,unreleased],
    u"k^h": [back,high,aspirated],
    u"k^y": [back,high,palletized],
    u"x": [back,high,continuant],
    u"X": [back,continuant], # χ
    u"x^y": [back,high,continuant,palletized],
    u"g": [back,high,voice],
    u"g^h": [back,high,voice,aspirated],
    u"g^y": [back,high,voice,palletized],
    u"ɣ": [back,high,continuant,voice],
    u"ɣ^y": [back,high,continuant,voice,palletized],
    u"ŋ": [back,high,nasal,voice,sonorant],#continuant],
    u"ŋ̩":  [back,high,nasal,voice,sonorant,syllabic],
    u"q": [back],
    u"N": [back,nasal,voice],#continuant],
    u"G": [back,voice],
    u"ʔ": [sonorant,low],#laryngeal,
    u"h": [continuant,sonorant,low],#laryngeal,
    u"ħ": [back, low,continuant,sonorant],

    # glides
    u"w": [glide,voice,sonorant,continuant],
    u"w̥": [glide,sonorant,continuant],
    u"y": [glide,palletized,voice,sonorant,continuant],
    u"j": [glide,palletized,voice,sonorant,continuant],

    # liquids
    u"r": [liquid,voice,coronal,sonorant,continuant],
    u"r̃": [liquid,trill,voice,coronal,sonorant,continuant],
    u"r̥̃": [liquid,trill,coronal,sonorant,continuant],
    u"ř": [liquid,flap,voice,coronal,sonorant,continuant],
    u"l": [liquid,lateral,voice,coronal,sonorant,continuant],
    u"l`": [liquid,secondStress,lateral,voice,coronal,sonorant,continuant],
    u"l̥": [liquid,lateral,coronal,sonorant,continuant],
    u"ʎ": [liquid,lateral,voice,palatal,sonorant,continuant],
    u"ł": [liquid,lateral,voice,back,high,sonorant,continuant],
#    u"̌l": [liquid,lateral,voice,coronal,sonorant],

    # I'm not sure what this is
    # I think it is a mistranscription, as it is in IPA but not APA
    # u"ɲ": []

    u"ʕ": [back, low, voice,continuant],
    u"-": [syllableBoundary],
    u"##": [wordBoundary],
}

simpleFeatureMap = {
    u"*": [wildFeature],
    u"?": [optionalFeature],
    
    # unrounded vowels
    u"i": [voice,tense,high,front],
    u"ɨ": [voice,tense,high,back,central],
    u"ɩ": [voice,high,front],
    u"e": [voice,tense,middle,front],
    u"ə": [voice,tense,middle,central],
    u"ɛ": [voice,middle,front],
    u"æ": [voice,low,front,tense],
    u"a": [voice,low,central,tense],
    u"ʌ": [voice,middle,central],
    # rounded vowels
    u"u": [voice,tense,high,back,rounded],
    u"ü": [voice,tense,high,front,rounded],
    u"ʊ": [voice,high,back,rounded],
    u"o": [voice,middle,tense,back,rounded],
    u"ö": [voice,middle,tense,front,rounded],
    u"ɔ": [voice,middle,back,rounded],
    #possibly missing are umlauts

    # consonance
    u"p": [bilabial,stop],
    u"p^y": [bilabial,stop,palletized],
    u"p̚": [bilabial,stop,unreleased],
    u"p^h": [bilabial,stop,aspirated],
    u"b": [bilabial, stop, voice],
    u"b^h": [bilabial, stop, voice, aspirated],
    u"f": [labiodental,fricative],
    u"φ": [bilabial,fricative],
    u"φ|": [bilabial,fricative],
    u"f^y": [labiodental,fricative,palletized],
    u"v": [labiodental,fricative,voice],
    u"β": [labiodental,fricative,voice],
    u"β|": [bilabial,fricative,voice],
    u"m": [bilabial,nasal,voice],
    u"m̩": [bilabial,nasal,voice,syllabic],
    u"m̥": [bilabial,nasal],#,continuant],
    u"θ": [dental, fricative],
    u"d": [alveolar,stop,voice],
    #u"d̪": [voice,coronal],
    u"d^z": [alveolar,affricate,voice],
    u"d^z^h": [alveolar,affricate,voice, aspirated],
    u"t": [alveolar, stop],
    u"t̚": [alveolar, stop, unreleased],
    u"t^s": [alveolar, affricate],
    u"t^h": [alveolar, stop,aspirated],
    u"ṭ": [alveolar, stop,retroflex],
    u"ḍ": [alveolar, stop,voice,retroflex],
    u"ṛ": [alveolar, fricative,retroflex,voice],
    u"ð": [dental, fricative, voice],
    u"z": [fricative, voice, alveolar],
    u"ǰ": [voice,alveopalatal,affricate],
    u"ž": [voice,alveopalatal,fricative],
    u"ž^y": [voice,alveopalatal,fricative,palletized],
    u"s": [fricative, alveolar],
    u"ṣ":  [fricative, alveolar, retroflex],
    u"n": [alveolar,nasal,voice],
    u"n̩": [alveolar,nasal,voice,syllabic],
    u"ṇ": [retroflex,nasal,voice],
    u"n̥": [alveolar,nasal],
    u"ñ": [nasal,voice,alveopalatal],
    u"n̆": [nasal,voice,alveopalatal],
    u"š": [fricative, alveopalatal],
    u"c": [palatal,stop],
    u"ç": [fricative,palatal],
    u"ɉ": [voice,palatal,stop],
    u"x̯": [palatal,fricative],
    u"č": [alveopalatal,affricate],
    u"č^y": [alveopalatal,affricate,palletized],
    u"č^h": [alveopalatal,affricate,aspirated],
    u"k": [velar, stop],
    u"k̚": [velar, stop,unreleased],
    u"k^h": [velar, stop,aspirated],
    u"k^y": [velar, stop,palletized],
    u"x": [velar, fricative],
    u"X": [fricative, uvular], # χ
    u"x^y": [velar, fricative,palletized],
    u"g": [velar, stop, voice],
    u"g^h": [velar, stop, voice, aspirated],
    u"g^y": [velar,stop,voice,palletized],
    u"ɣ": [velar,fricative,voice],
    u"ɣ^y": [velar,fricative,voice,palletized],
    u"ŋ": [velar,nasal,voice],
    u"ŋ̩": [velar,nasal,voice,syllabic],
    u"q": [uvular, stop],
    u"N": [uvular, nasal,voice],#continuant],
    u"G": [uvular, stop,voice],
    u"ʔ": [laryngeal,stop],
    u"h": [laryngeal,fricative],
    u"ħ": [pharyngeal,fricative],

    # glides
    u"w": [glide,voice,bilabial],
    u"w̥": [glide,bilabial],
    u"y": [glide,voice],
    u"j": [glide,palletized,voice],

    # liquids
    u"r": [liquid,voice,retroflex],
    u"r̃": [liquid,trill,voice,retroflex],
    u"r̥̃": [liquid,trill,retroflex],
    u"ř": [liquid,flap,voice,retroflex],
    u"l": [liquid,lateral,voice],
    u"l`": [secondStress,liquid,lateral,voice],
    u"l̥": [liquid,lateral],
    u"ʎ":  [liquid,lateral,palatal,voice],
    u"ł": [liquid,lateral,voice,velar],
#    u"̌l": [liquid,lateral,voice,coronal,sonorant],

    # I'm not sure what this is
    # I think it is a mistranscription, as it is in IPA but not APA
    u"ɲ": [nasal,voice,alveopalatal,high],
    u"ɲ̩": [nasal,voice,alveopalatal,high,syllabic],

    u"ʕ": [affricate, pharyngeal, voice],
    u"-": [syllableBoundary],
    u"##": [wordBoundary],
}

featureMap = sophisticatedFeatureMap


# Automatically annotate vowels
vs = [u"i",u"ɨ",u"ɩ",u"e",u"ə",u"ɛ",u"æ",u"a",u"ʌ",u"u",u"ü",u"ʊ",u"o",u"ö",u"ɔ"]
for fm in [simpleFeatureMap, sophisticatedFeatureMap]:
    for k in fm:
        features = featureMap[k]
        if k in vs:
            features.append(vowel)
# feature set only apply to vowels
VOWELFEATURES = {rounded, tense, low, longVowel, risingTone, lowTone, highTone, middleTone}

# feature set only apply to consonants
CONSONANTFEATURES = {aspirated,palletized}

CONSONANTPLACEFEATURES = {anterior,coronal}

# features that always apply to vowels
DEFAULTVOWELFEATURES = {sonorant,continuant}

# Include vowel/consonants diacritics
vs = [ k for k in featureMap if vowel in featureMap[k] ]
cs = [ k for k in featureMap if not (vowel in featureMap[k]) ]
for fm in [simpleFeatureMap, sophisticatedFeatureMap]:
    for v in vs:
        if fm == sophisticatedFeatureMap:
            fm[v] += list(DEFAULTVOWELFEATURES)
        fm[v + u"́"] = fm[v] + [highTone]
        fm[v + u"`"] = fm[v] + [lowTone]
        fm[v + u"¯"] = fm[v] + [middleTone]
        fm[v + u":"] = fm[v] + [longVowel]
        fm[v + u"́:"] = fm[v] + [longVowel,highTone]
        fm[v + u"̌"] =  fm[v] + [risingTone]
        fm[v + u"̃"] = fm[v] + [nasal]
# Mohawk is crazy like this
v = u"ʌ"
for fm in [simpleFeatureMap, sophisticatedFeatureMap]:
    fm[v + u"̃́"] = fm[v] + [nasal,highTone]
    fm[v + u"̃́:"] = fm[v] + [nasal,highTone,longVowel]



# palletization
for fm in [simpleFeatureMap, sophisticatedFeatureMap]:
    for p in [u'v',u'b',u't',u'z',u'š',u'l',u'd',u'm',u's',u't^s',u'n',u'r']:
        fm[p + u'^y'] = fm[p] + [palletized]

# Let's give sonority to the simple features also
for p,f in sophisticatedFeatureMap.iteritems():
    if "sonorant" in f:
        assert "sonorant" not in simpleFeatureMap[p]
        simpleFeatureMap[p].append("sonorant")
        

def tokenize(word):
    # š can be realized in two different ways
    if u"š" in word:
        print u"ERROR: š should have been purged."
        print "word =",word
        assert False
    # FIXME: this is not part of APA, approximate with a shewha
    word = word.replace(u"ɜ", u"ə")
    # remove all the spaces
    word = word.replace(u" ",u"")
    # not sure what this is but let's remove it
    word = word.replace(u"’",u"")
    # IPA > APA
    word = word.replace(u"ɪ",u"ɩ")
    originalWord = word
    tokens = []
    while len(word) > 0:
        # Find the largest prefix which can be looked up in the feature dictionary
        for suffixLength in range(len(word)):
            prefixLength = len(word) - suffixLength
            prefix = word[:prefixLength]
            if prefix in featureMap:
                tokens.append(prefix)
                word = word[prefixLength:]
                break
            elif suffixLength == len(word) - 1:
                print word
                print originalWord
                raise Exception(u"No valid prefix: " + word + u" when parsing " + originalWord + "into phonemes. Perhaps you are trying to use a phoneme that is not currently part of the system.")
    return tokens

class FeatureBank():
   
    """Builds a bank of features and sounds that are specialized to a particular data set.
    The idea is that we don't want to spend time reasoning about features/phonemes that are not attested"""
    mutuallyExclusiveClasses = []#["stop","fricative","affricate"]]
    
    def __init__(self, words):
        self.phonemes = list(set([ p for w in words for p in (tokenize(w) if isinstance(w,unicode) else w.phonemes) ]))
        self.features = list(set([ f for p in self.phonemes for f in featureMap[p] ]))
        self.featureMap = {p: list(set(featureMap[p]) & set(self.features))
                           for p in self.phonemes }
        self.featureVectorMap = {p: [ (f in self.featureMap[p]) for f in self.features ]
                                 for p in self.phonemes }
        self.phoneme2index = dict([ (self.phonemes[j],j) for j in range(len(self.phonemes)) ])
        self.feature2index = dict([ (self.features[j],j) for j in range(len(self.features)) ])
        self.matrix2phoneme = dict([ (frozenset(featureMap[p]),p) for p in self.phonemes ])

        self.hasSyllables = syllableBoundary in self.features

        # if len(self.phonemes) < 80 and False:
        #     print "%d possible structural changes"%(len(self.possibleStructuralChanges()))
        #     print("%d possible guards"%(len(self.possibleGuards())))
        # for p in self.phonemes:
        #     print p,"\t",self.makeNasal(p)

    def checkCollisions(self):
        for p in self.featureVectorMap:
            for q in self.featureVectorMap:
                if p == q: continue
                if self.featureVectorMap[p] == self.featureVectorMap[q]:
                    print "WARNING: these have the same feature vectors in the bank:",p,q
                    print "The features are",self.featureVectorMap[p]
                    print featureMap[p]
                    print featureMap[q]
                    assert False        

    def possibleStructuralChanges(self):
        import itertools
        from rule import FeatureMatrix
        
        def extension(fm):
            e = set()
            for p in self.phonemes:
                pp = frozenset(fm.apply(self.featureMap[p]))
                pp = self.matrix2phoneme.get(pp, None)
                if pp is not None:
                    e.add((p,pp))
            return frozenset(e)
        extension2matrix = {}
        for cost in range(1,4):
            for features in itertools.combinations(self.features, cost):
                for polarities in itertools.product(*([(True,False)]*cost)):
                    matrix = FeatureMatrix(zip(polarities, features))
                    e = extension(matrix)
                    if e not in extension2matrix:
                        extension2matrix[e] = matrix
        extension2matrix = {e:m for e,m in extension2matrix.iteritems()
                            if not any( ep > e for ep in extension2matrix if e != ep )}
        return extension2matrix

    def possibleGuards(self):
        import itertools
        from rule import FeatureMatrix

        extension2matrix = {}
        for cost in range(1,4):
            for features in itertools.combinations(self.features, cost):
                for polarities in itertools.product(*([(True,False)]*cost)):
                    matrix = FeatureMatrix(zip(polarities, features))
                    e = frozenset(matrix.extension(self))
                    if len(e) > 0 and e not in extension2matrix:
                        extension2matrix[e] = matrix
        return extension2matrix

    def assimilatePlace(self, target, source):
        placeFeatures = [anterior, coronal, high, back, low]
        target = self.featureMap[target]
        if u"ŋ" in self.phonemes and nasal in target and source == u"h": return u"ŋ"
        if u"ɲ̩" in self.phonemes and nasal in target and source in [u"ǰ"]:
            if syllabic in target: return u"ɲ̩"
            else: return u"ɲ"
        if u"ɲ" in self.phonemes and nasal in target and source in [u"ç",u"ɉ",u"ǰ",u"č"]: return u"ɲ"
        
        source = self.featureMap[source]
        
        for f in placeFeatures:
            if f in source: target = target + [f]
            else: target = [_f for _f in target if f != _f ]
        target = set(target)
        
        destination,_ = min(list(self.featureMap.iteritems()),
                            key=lambda pf: len(target^set(pf[1])))
        if False:
            lowest_score = len(target^set(self.featureMap[destination]))
            for pf in self.featureMap.iteritems():
                score = len(target^set(pf[1]))
                if score == lowest_score and pf[0] != destination:
                    print "ambiguity: target=",targetPhoneme,"source=",sourcePhoneme,"gt=",destination,"vs=",pf[0]
        
        return destination

    def calculatePlaceMapping(self):
        """Returns {target: [(new form, sources)]}"""
        possiblePhonemes = {p for p,f in self.featureMap.iteritems()
                            if vowel not in f and syllableBoundary not in f and wordBoundary not in f \
                            and wildFeature not in f and optionalFeature not in f}
        mapping = {}
        for target in possiblePhonemes:
            mapping[target] = []
            newForms = {self.assimilatePlace(target, source)
                        for source in possiblePhonemes }
            for newForm in newForms:
                sources = {source
                           for source in possiblePhonemes
                           if self.assimilatePlace(target, source) == newForm}
                mapping[target].append((newForm, sources))
        return mapping

    
    def definePlaceAssimilation(self):
        mapping = self.calculatePlaceMapping()
        m = "#define PLACEASSIMILATION\nSound assimilatePlace(Sound source, Sound target) {\n"
        for target in mapping:
            m += "  if (target == phoneme_%d) {\n"%(self.phoneme2index[target])
            for newForm, sources in mapping[target]:
                condition = " || ".join("source == phoneme_%d"%self.phoneme2index[s]
                                        for s in sources)
                m += "    if (%s) return phoneme_%d;\n"%(condition, self.phoneme2index[newForm])
            m += "    assert 0;}\n"
        m += "  assert 0;}\n"
        return m

    def defineMakeNasal(self):
        m = "#define ONLYNASAL(v) %s"%(" && ".join( "!v.%s_specified"%f if f != nasal else "v.%s_specified&&v.%s"%(f,f)
                                                    for f in self.features ))
        m += "\n#define MAKENASAL\nSound makeNasal(Sound source){\n"
        for p in self.phonemes:
            q = self.makeNasal(p)
            m += "  if (source == phoneme_%d) "%(self.phoneme2index[p])
            if q is None:
                m += "assert 0;\n"
            else:
                m += "return phoneme_%d;\n"%(self.phoneme2index[q])
        m += "}\n"
        return m
    
    def makeNasal(self, target):
        if target in [u"b",u"p"] and u"m" in self.phonemes: return u"m"
        if target in [u"d",u"s",u"t"] and u"n" in self.phonemes: return u"n"
        target = set(self.featureMap[target])
        if vowel in target or nasal in target: return None
        target.add(nasal)
        target.add(sonorant)
        nasals = {p for p,f in self.featureMap.iteritems()
                  if nasal in f and vowel not in f}
        if len(nasals) == 0: return None
        bestScore = None
        bestNasal = None
        for n in nasals:
            score = len(target^set(self.featureMap[n]))
            if bestScore is None:
                bestScore = score
                bestNasal = n
            elif bestScore == score: return None # ambiguity
            elif bestScore > score:
                bestScore = score
                bestNasal = n
        return bestNasal
        
            

    @staticmethod
    def fromData(d):
        return FeatureBank([ w for i in d for w in i if w != None ])
        
    def wordToMatrix(self, w):
        return [ self.featureVectorMap[p] for p in tokenize(w) ]
    
    def variablesOfWord(self, w):
        tokens = tokenize(w)
        p2v = dict([ (self.phonemes[j],j) for j in range(len(self.phonemes)) ])
        return [ "phoneme_%d" % p2v[t] for t in tokens ]

    def defineFeaturesToSound(self):
        d = "Sound features2sound(bit[NUMBEROFFEATURES] f){\n"
        for j,p in enumerate(self.phonemes):
            d += "if (f == {%s})" % (",".join(map(str,self.featureVectorMap[p])))
            d += " return phoneme_%d;\n"%j
        d += "assert 0;}\n"
        return d

    def defineSound(self):
        h = "\nstruct Sound{//@Immutable(\"\")\n"
        for f in self.features:
            h += "  bit %s;\n"%(f)
        h += "}\n"
        return h
    def defineVector(self):
        h = "\n#define DEFINEVECTOR struct Vector extends Specification{@Immutable(\"\")\\\n"
        for f in self.features:
            h += "  bit %s_specified; bit %s;\\\n"%(f,f)
        h += "}\n\n"
        h += "\n#define VECTOREQUAL(p,q) (%s)\n"%(" && ".join([ "p.%s_specified == q.%s_specified"%(f,f)
                                                                for f in self.features] + \
                                                              ["(p.%s_specified && p.%s) == (q.%s_specified && q.%s)"%(f,f,f,f)
                                                                for f in self.features]))
        h += "\n#define EMPTYVECTOR(v) (%s)\n"%(" && ".join("v.%s_specified == 0"%f
                                                            for f in self.features))
        h += "\n#define VECTORCOST(v) "
        c = "0"
        for f in self.features:
            c = "validateCost(v.%s_specified + %s)"%(f,c)
        h += c + "\n"

        h += "\n#define VECTORMATCHESSOUND(vector, sound) (%s)\n"%(" && ".join("(!vector.%s_specified || vector.%s == sound.%s)"%(f,f,f)
                                                                               for f in self.features))
        h += "\n#define PROJECTVECTOR(vector, sound)\\\n"
        for f in self.features:
            h += "  bit %s = (!vector.%s_specified && sound.%s) || (vector.%s_specified && vector.%s);\\\n"%(f,f,f,f,f)
        for p in self.phonemes:
            condition = " && ".join("%s%s"%("" if f in featureMap[p] else "!", f)
                                    for f in self.features)
            h += "  if (%s) return phoneme_%d;\\\n"%(condition, self.phoneme2index[p])
        h += "assert 0;\\\n\n"

        h += "\n#define UNKNOWNVECTOR %s\n"%(", ".join( "%s = ??, %s_specified = ??"%(f,f)
                                                        for f in self.features))        
        return h

    def defineZeroFeatures(self):
        z = "#define ZEROFEATURES(m) ({"
        m = "#define MUTUALLYEXCLUDE(s) "
        for f in self.features:
            excluded = False
            for k in FeatureBank.mutuallyExclusiveClasses:
                if f in k:
                    assert not excluded
                    # only retain other members of the class which are actually used in the data
                    kp = set(k) & set(self.features)

                    # mutual exclusion logic
                    m += "if (s.mask[%d]) assert s.preference[%d] "%(self.feature2index[f], self.feature2index[f])
                    m += " && ".join([''] + [ "!s.mask[%d]"%(self.feature2index[e]) for e in kp if e != f ])
                    m += '; '
                    
                    if len(kp) > 1:
                        z += "||".join([ "m[%d]"%(self.feature2index[e]) for e in kp if e != f ])
                        excluded = True
            if not excluded: z += "0"
            z += ", "

        # replace the final, with a }
        return z[:-2] + '})\n' + m

    def __unicode__(self):
        return u'FeatureBank({' + u','.join(self.phonemes) + u'})'
    def __str__(self): return unicode(self).encode('utf-8')

    def phonemeConstant(self,p):
        from sketchSyntax import Constant
        return Constant("phoneme_%d"%(self.phoneme2index[p]))

    def sketch(self, placeAssimilation = False, nasalAssimilation = False):
        """Sketches definitions of the phonemes in the bank"""
        for p in self.featureVectorMap:
            for q in self.featureVectorMap:
                if p == q: continue
                if self.featureVectorMap[p] == self.featureVectorMap[q]:
                    print "WARNING: these have the same feature vectors in the bank:",p,q
                    print "The features are",self.featureVectorMap[p]
                    print featureMap[p]
                    print featureMap[q]
                    assert False
        
        h = ""
        h += self.defineSound()
        h += self.defineVector()
        if self.hasSyllables:
            h += "#define SYLLABLEBOUNDARYPHONEME phoneme_%d\n"%(self.phoneme2index[u"-"])
            h += "#define SYLLABLEBOUNDARYFEATURE %d\n"%(self.feature2index[syllableBoundary])
        if u'*' in self.phonemes:
            h += "#define WILDPATTERN phoneme_%d\n"%(self.phoneme2index[u"*"])
        if u'?' in self.phonemes:
            h += "#define MAYBEPATTERN phoneme_%d\n"%(self.phoneme2index[u"?"])

        for j in range(len(self.phonemes)):
            features = ",".join("%s = %d"%(f, int(f in featureMap[self.phonemes[j]]))
                for f in self.features)
            h += "Sound phoneme_%d = new Sound(%s);\n" % (j,features)
        h += "#define UNKNOWNSOUND {| %s |}" % (" | ".join(["phoneme_%d"%j for j in range(len(self.phonemes))
                                                            if self.phonemes[j] != u'-' ]))
        h += "\n#define UNKNOWNCONSTANTSPECIFICATION {| %s |}\n" % (" | ".join(["phoneme_%d"%j for j in range(len(self.phonemes)) ]))
        
        h += "\n"

        if placeAssimilation:
            h += self.definePlaceAssimilation() + "\n"
        if nasalAssimilation and nasal in self.features:
            h += self.defineMakeNasal() + "\n"
        return h

FeatureBank.GLOBAL = FeatureBank(featureMap.keys())
FeatureBank.ACTIVE = None

def switchFeatures(f):
    global featureMap
    assert f in ['sophisticated','simple']
    if f == 'sophisticated':
        featureMap = sophisticatedFeatureMap
    elif f == 'simple':
        featureMap = simpleFeatureMap
    else: assert False
    FeatureBank.GLOBAL = FeatureBank(featureMap.keys())


def minimumCostAlignment(surfaces, N=1, table=None):
    if table is None:
        table = {}
        surfaces = tuple(map(tuple,surfaces))
    else:
        if surfaces in table:
            return table[surfaces]
    
    from utilities import PQ, isPowerOf
    
    INSERTIONCOST = 3
    def alignmentCost(indexes, differences):
        aligned = [surfaces[j][i]
                   for j,i,d in zip(xrange(100),indexes,differences)
                   if d == 1 ]
        def phonemeCost(p1,p2):
            return len(set(featureMap[p1])^set(featureMap[p2]))
        c1 = min( sum( phonemeCost(p,q) for q in aligned )
                  for p in aligned )
        c2 = INSERTIONCOST*sum(d == 0 for d in differences )
        return c1 + c2
        
    class State():
        def __init__(self, indexes, cost, parent):
            # indexes: how much of the surface we have consumed
            self.parent = parent
            self.indexes = indexes
            self.cost = cost
        def __eq__(self,o): return tuple(self.indexes) == tuple(o.indexes)
        def __ne__(self,o): return not (self == o)
        def __hash__(self): return hash(tuple(self.indexes))
        
        @property
        def terminal(self):
            return all( j == len(s) for j,s in zip(self.indexes,surfaces)  )
        def ur(self):
            if self.parent is None: return []
            u = self.parent.ur()
            advances = []
            for j, (myIndex,parentIndex) in enumerate(zip(self.indexes, self.parent.indexes)):
                if myIndex == parentIndex:
                    advances.append(None)
                else:
                    assert myIndex == parentIndex + 1
                    advances.append(surfaces[j][parentIndex])
            advances = set(advances)
            if len(advances) == 1:
                return u + [list(advances)[0]]
            else:
                return u + [advances]

        def showTrace(self):
            if self.parent is None:
                print("Initialize match")
                return
            self.parent.showTrace()
            print("Next advances: (cost=%d)"%self.cost)
            print(", ".join( str(myIndex - parentIndex) for myIndex,parentIndex in zip(self.indexes, self.parent.indexes) ))

        def h(self):
            """Heuristic: lower bound on the cost to go
            Heuristic is to take the smallest alignment of any pair"""
            if len(self.indexes) <= 2: return 0
            return 0
            return min( minimumCostAlignment( (surfaces[j][self.indexes[j]:],
                                               surfaces[k][self.indexes[k]:]),
                                              N=1,
                                              table=table)[0].cost
                        for j in xrange(len(self.indexes) - 1)
                        for k in xrange(j + 1, len(self.indexes)) )
        def g(self):
            return self.h() + self.cost
            
            
        def children(self):
            if self.terminal: return

            # Special case: everything is perfectly aligned
            if all( i < len(s) for i,s in zip(self.indexes, surfaces) ) and \
               all( s[i] == surfaces[0][self.indexes[0]] for i,s in zip(self.indexes, surfaces) ):
                yield State([ 1 + i for i in self.indexes ],
                            self.cost,
                            self)
                return 

            def d(n):
                if n == 0:
                    yield []
                    return
                for j in [0,1]:
                    for s in d(n - 1):
                        yield [j] + s
            for ds in d(len(surfaces)):
                if sum(ds) > 0:
                    if any( i+di > len(s) for s,i,di in zip(surfaces,self.indexes,ds)  ):
                        continue
                    
                    dc = alignmentCost(self.indexes, ds)                    
                    yield State([i + di for i,di in zip(self.indexes,ds) ],
                                self.cost + dc,
                                self)

    frontier = PQ()
    s0 = State([0]*len(surfaces),0,None)
    frontier.push(-s0.cost, s0)
    visited = {}

    finished = []
    while True:
        s = frontier.popMaximum()
        if s.terminal:
            finished.append(s)
            if len(finished) >= N:
                table[surfaces] = finished
                return finished
        else:
            for c in s.children():
                if c not in visited:
                    visited[c] = True
                    frontier.push(-c.g(), c)

    


if __name__ == "__main__":
    vs = [ k for k,v in sophisticatedFeatureMap.iteritems() if vowel in v]
    def show(p):
        if p in [u'##',u'*',u'-',u'?']: return 
        print p,"\t","[ %s ]"%(" ".join([ "+"+f for f in sorted(sophisticatedFeatureMap[p])]))
    
    def showMany(name, ps):
        print "%s:"%name
        for p in sorted(ps):
            show(p)
        print
    showMany("vowels", vs)
    showMany("nasals", [ k for k,v in sophisticatedFeatureMap.iteritems() if vowel not in v and nasal in v])
    showMany("consonants", [ k for k,v in sophisticatedFeatureMap.iteritems() if vowel not in v and nasal not in v])
