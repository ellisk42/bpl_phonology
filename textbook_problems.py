# -*- coding: utf-8 -*-
from problems import *


# Odden's Introducing Phonology
Odden_Problems = []

Odden_Problems.append(Problem(
	u'''
Russian Odden 68-69''',
	[
	# Nominative sg		Genitive sg  		Gloss
	(u"vagon",			u"vagona"),			# wagon
	(u"avtomobil^y",	u"avtomobil^ya"),	# car
	(u"večer",			u"večera"),			# evening
	(u"muš",			u"muža"),			# husband
	(u"karandaš",		u"karandaša"),		# pencil
	(u"glas",			u"glaza"),			# eye
	(u"golos",			u"golosa"),			# voice
	(u"ras",			u"raza"),			# time
	(u"les",			u"lesa"),			# forest
	(u"porok",			u"poroga"),			# threshold
	(u"vrak",			u"vraga"),			# enemy
	(u"urok",			u"uroka"),			# lesson
	(u"porok",			u"poroka"),			# vice
	(u"t^svet",			u"t^sveta"),		# color
	(u"prut",			u"pruda"),			# pond
	(u"soldat",			u"soldata"),		# soldier
	(u"zavot",			u"zavoda"),			# factory
	(u"xlep",			u"xleba"),			# bread
	(u"grip",			u"griba"),			# mushroom
	(u"trup",			u"trupa")			# corpse
	], 
	solutions = [u'''
stem
stem + a
[-sonorant] -> [-voice] / _ #
	''']))

Odden_Problems.append(Problem(
	u'''
Finnish Odden 73-74	
	''',
	[ 
	# a. Nominative sg		Partitive sg  		Gloss
	(u"aamu",			u"aamua"),			# morning
	(u"hopea",			u"hopeaa"),			# silver
	(u"katto",			u"kattoa"),			# roof
	(u"kello",			u"kelloa"),			# clock
	(u"kirya",			u"kiryaa"),			# book
	(u"külmæ",			u"külmææ"),			# cold
	(u"koulu",			u"koulua"),			# school
	(u"lintu",			u"lintua"),			# bird
	(u"hüllü",			u"hüllüæ"),			# shelf
	(u"kömpelö",		u"kömpelöæ"),		# clumsy
	(u"nækö",			u"næköæ"),			# appearance

	# b. Nominative sg		Partitive sg  		Gloss
	(u"yoki",			u"yokea"),			# river
	(u"kivi",			u"kiveæ"),			# stone
	(u"muuri",			u"muuria"),			# wall
	(u"naapuri",		u"naapuria"),		# neighbor
	(u"nimi",			u"nimeæ"),			# name
	(u"kaappi",			u"kaappia"),		# chest of drawers
	(u"kaikki",			u"kaikkea"),		# all
	(u"kiirehti",		u"kiirehtiæ"),		# hurry
	(u"lehti",			u"lehteæ"),			# leaf
	(u"mæki",			u"mækeæ"),			# hill
	(u"ovi",			u"ovea"),			# door
	(u"posti",			u"postia"),			# mail
	(u"tukki",			u"tukkia"),			# log
	(u"æiti",			u"æitiæ"),			# mother
	(u"englanti",		u"englantia"),		# England
	(u"yærvi",			u"yærveæ"),			# lake
	(u"koski",			u"koskea"),			# waterfall
	(u"reki",			u"rekeæ"),			# sledge
	(u"væki",			u"vækeæ")			# people
	], 
	solutions = [u'''
stem
stem + æ
e ---> [ +high ] /  _ #
æ ---> [ +back ] / [ +back +continuant ] [  ]* _
	''']))

Odden_Problems.append(Problem(
	u'''
Kerewe Odden 76-77	
	''',
	[ 
	# Infinitive		1sg habitual		3sg habitual		Imperative		Gloss

	(u"kupaamba",		u"mpaamba",			u"apaamba",			u"paamba"),		# adorn
	(u"kupaaŋga",		u"mpaaŋga",			u"apaaŋga",			u"paaŋga"),		# line up
	(u"kupima",			u"mpima",			u"apima",			u"pima"),		# measure
	(u"kupuupa",		u"mpuupa",			u"apuupa",			u"puupa"),		# be light
	(u"kupekeča",		u"mpekeča",			u"apekeča",			u"pekeča"),		# make fire with stick
	(u"kupiinda",		u"mpiinda",			u"apiinda",			u"piinda"),		# be bent
	(u"kuhiiga",		u"mpiiga",			u"ahiiga",			u"hiiga"),		# hunt
	(u"kuheeka",		u"mpeeka",			u"aheeka",			u"heeka"),		# carry
	(u"kuhaaŋga",		u"mpaaŋga",			u"ahaaŋga",			u"haaŋga"),		# create
	(u"kuheeba",		u"mpeeba",			u"aheeba",			u"heeba"),		# guide
	(u"kuhiima",		u"mpiima",			u"ahiima",			u"hiima"),		# gasp
	(u"kuhuuha",		u"mpuuha",			u"ahuuha",			u"huuha")		# breath into
	], 
	solutions = [u'''
ku + stem + a
m + stem + a
a + stem + a
stem + a

# postnasal hardening
[-voice] -> p / [+nasal] _
	''']
	))


Odden_Problems.append(Problem(
	u'''
English Odden 77-78	
	''',
	[ 
	## Noun Plural Suffix

	# suffix [s]		
	(u"kæps",),		# caps
	(u"kæts",),		# cats
	(u"kaks",),		# cocks
	(u"pruwfs",),	# proofs

	# suffix [z]		
	(u"kæbz",),		# cabs
	(u"kædz",),		# cads
	(u"kagz",),		# cogs
	(u"hʊvz",),		# hooves
	(u"fliyz",),	# fleas
	(u"plæwz",),	# plows
	(u"pyṛez",),	# purees

	(u"klæmz",),	# clams
	(u"kænz",),		# cans
	(u"karz",),		# cars
	(u"gəlz",),		# gulls
	

	## 3sg Present Verbal Suffix

	# suffix [s]
	(u"slæps",),	# slaps
	(u"hɩts",),		# hits
	(u"powks",),	# pokes

	# suffix [z]
	(u"stæbz",),	# stabs
	(u"haydz",),	# hides
	(u"dɩgz",),		# digs
	(u"læfs",),		# laughs
	(u"pɩθs",),		# piths

	(u"slæmz",),	# slams
	(u"kænz",),		# cans
	(u"hæŋz",),		# hangs
	(u"θrayvz",),	# thrives
	(u"beyðz",),	# bathes
	(u"flayz",)		# flies

	], 
	solutions = [u'''
stem + z
[-sonorant] -> [-voice] / [-voice] _
	''']))


Odden_Problems.append(Problem(
	u'''
Jita Odden 79
	''',
	[ 
	(u"okuβuma",		# to hit
	 u"okuβumira",		# to hit for
	 u"okuβumana",		# to hit each other
	 u"okuβumirana",	# to hit for each other
	 u"okumuβúma",		# to hit him/her
	 u"okumuβúmira",	# to hit for him/her
	 u"okučiβúma",		# to hit it
	 u"okučiβúmira"),	# to hit for it
            

	(u"okusiβa",		# to block
	 u"okusiβira",		# to block for
	 u"okusiβana",		# to block each other
	 u"okusiβirana",	# to block for each other
     u"okumusíβa",		# to block him/her
	 u"okumusíβira",	# to block for him/her
	 u"okučisíβa",		# to block it
	 u"okučisíβira"),	# to block for it

	(u"okulúma",		# to bite
	 u"okulumíra",		# to bite for
	 u"okulumána",		# to bite each other
	 u"okulumírana",	# to bite for each other
         None,None,None,None),

	(u"okukúβa",		# to fold
	 u"okukuβíra",		# to fold for
	 u"okukuβána",		# to fold each other
	 u"okukuβírana",	# to fold for each other
         None,None,None,None)

	], 
	solutions = [u'''
oku + stem + a
oku + stem + ir + a
oku + stem + an + a
oku + stem + ir + an + a

oku + mú + stem + a
oku + mú + stem + ir + a
oku + čí + stem + a
oku + čí + stem + ir + a

# High tone shifting
[+highTone]C[-highTone] > [-highTone]C[+highTone]
	''']
	))




Odden_Problems.append(Problem( # RERUN
	u'''
Korean Odden 81
	''',
	[ 
	# Imperative	Plain Present		Gloss

	(u"ana",		u"annɨnta"),		# hug
	(u"kama",		u"kamnɨnta"),		# wind
	(u"sinə",		u"sinnɨnta"),		# wear shoes
	(u"t̚atɨmə",		u"t̚atɨmnɨnta"),		# trim
	(u"nəmə",		u"nəmnɨnta"),		# overflow
	(u"nama",		u"namnɨnta"),		# remain
	(u"č^hama",		u"č^hamnɨnta"),		# endure
	(u"ipə",		u"imnɨnta"),		# put on
	(u"kupə", 		u"kumnɨnta"),		# bend
	(u"čəpə", 		u"čəmnɨnta"),		# fold
	(u"tata",	 	u"tannɨnta"),		# close
	(u"put^hə", 	u"punnɨnta"),		# adhere
	(u"čoč^ha", 	u"čonnɨnta"),		# follow
	(u"məkə", 		u"məŋnɨnta"),		# eat
	(u"sək̚ə", 		u"səŋnɨnta"),		# mix
	(u"tak̚a", 		u"taŋnɨnta"),		# polish
	(u"čukə",	 	u"čuŋnɨnta"),		# die
	(u"ikə", 		u"iŋnɨnta")			# ripen
	],
	solutions = [u'''
stem + ə
stem + nɨnta

    [ +aspirated ] > [ -aspirated ] / _ C ; this test case will pass even if this is not included
    ə > a / a C* _
        [-sonorant] > [+nasal] / _[+nasal]

	''']
	))


Odden_Problems.append(Problem(
	u'''
Koasati Odden 81
	''',
	[ 
	# Noun			1st-sg-pos("my") + N	Gloss
	(u"apahčá",		u"amapahčá"),			# shadow
	(u"asikčí",		u"amasikčí"),			# muscle
	(u"ilkanó",		u"amilkanó"),			# right side
	(u"ifá",		u"amifá"),				# dog
	(u"a:pó",		u"ama:pó"),				# grandmother
	(u"iskí",		u"amiskí"),				# mother
	(u"pačokkö́ka",	u"ampačokkö́ka"),		# chair
	(u"towá",		u"antowá"),				# onion
	(u"kastó",		u"aŋkastó"),			# flea
	(u"bayá:na",	u"ambayá:na"),			# stomach
	(u"tá:ta",		u"antá:ta"),			# father
	(u"čofkoní",	u"añčofkoní"),			# bone
	(u"kitiłká",	u"aŋkitiłká"),			# hair bangs
	(u"toní",		u"antoní")				# hip
	], 
	solutions = [u'''
stem
am + stem
        [+nasal] > place+1 / _ [-sonorant]
	''']
	))


Odden_Problems.append(Problem(
	u'''
Samoan Odden 85
	''',
	[ 
	# Simple		Perfective		Gloss
	(u"olo",		u"oloia"),		# rub
	(u"lafo",		u"lafoia"),		# cast
	(u"aŋa",		u"aŋaia"),		# face
	(u"usu",		u"usuia"),		# get up and go early
	(u"tau",		u"tauia"),		# reach a destination
	(u"taui",		u"tauia"),		# repay
	(u"sa:ʔili",	u"sa:ʔilia"),	# look for
	(u"vaŋai",		u"vaŋaia"),		# face each other
	(u"paʔi",		u"paʔia"),		# touch
	(u"naumati",	u"naumatia"),	# be waterless
	(u"sa:uni",		u"sa:unia"),	# prepare
	(u"seŋi",		u"seŋia"),		# be shy
	(u"lele",		u"lelea"),		# fly
	(u"suʔe",		u"suʔea"),		# uncover
	(u"taʔe",		u"taʔea"),		# smash
	(u"tafe",		u"tafea"),		# flow
	(u"ta:upule",	u"ta:upulea"),	# confer
	(u"palepale",	u"palepalea"),	# hold firm

	(u"tu:",		u"tu:lia"),		# stand
	(u"tau",		u"taulia"),		# cost
	(u"ʔalo",		u"ʔalofia"),	# avoid
	(u"oso",		u"osofia"),		# jump
	(u"sao",		u"saofia"),		# collect
	(u"asu",		u"asuŋia"),		# smoke
	(u"pole",		u"poleŋia"),	# be anxious
	(u"ifo",		u"ifoŋia"),		# bow down
	(u"ula",		u"ulaŋia"),		# mock
	(u"milo",		u"milosia"),	# twist
	(u"valu",		u"valusia"),	# scrape
	(u"vela",		u"velasia"),	# be cooked
	(u"api",		u"apitia"),		# be lodged
	(u"eʔe",		u"eʔetia"),		# be raised
	(u"lava:",		u"lava:tia"),	# be able
	(u"u:",			u"u:tia"),		# grip
	(u"puni",		u"punitia"),	# be blocked
	(u"siʔo",		u"siʔomia"),	# be enclosed
	(u"ŋalo",		u"ŋalomia"),	# forget
	(u"sopo",		u"sopoʔia"),	# go across

	(u"au",			u"aulia"),		# flow on
	(u"ma:tau",		u"ma:taulia"),	# observe
	(u"ili",		u"ilifia"),		# blow
	(u"ulu",		u"ulufia"),		# enter
	(u"taŋo",		u"taŋofia"),	# take hold
	(u"soa",		u"soaŋia"),		# have a friend
	(u"fesili",		u"fesiliŋia"),	# question
	(u"ʔote",		u"ʔoteŋia"),	# scold
	(u"tofu",		u"tofuŋia"),	# dive
	(u"laʔa",		u"laʔasia"),	# step
	(u"taŋi",		u"taŋisia"),	# cry
	(u"motu",		u"motusia"),	# break
	(u"mataʔu",		u"mataʔutia"),	# fear
	(u"sau",		u"sautia"),		# fall
	(u"oʔo",		u"oʔotia"),		# arrive
	(u"ufi",		u"ufitia"),		# cover
	(u"tanu",		u"tanumia"),	# cover up
	(u"moʔo",		u"moʔomia"),	# admire
	(u"tao",		u"taomia"),		# cover
	(u"fana",		u"fanaʔia")		# shoot
	], 
	solutions = [u'''
stem
stem + ia

# Vowel-cluster reduction
[ +vowel -back] -> 0 / [ +vowel -back ] _ 

# Final consonant deletion
 C -> 0 / _ #
	''']
	))

Odden_Problems.append(Problem(
	u'''
Palauan Odden 88
	''',
	[ 
	# Present middle	Future innovative	Future Conservative		Gloss
	(u"mədáŋəb",		u"dəŋəbáll",		u"dəŋóbl"),				# cover
	(u"mətéʔəb",		u"təʔəbáll",		u"təʔíbl"),				# pull out
	(u"məŋétəm",		u"ŋətəmáll",		u"ŋətóml"),				# lick
	(u"mətábək",		u"təbəkáll",		u"təbákl"),				# patch
	(u"məʔárəm",		u"ʔərəmáll",		u"ʔəróml"),				# taste
	(u"məsésəb",		u"səsəbáll",		u"səsóbl")				# burn
	], 
	solutions = [u'''
mə + stem
stem + al + l
stem + l

# final syllable stressed if ends in two consonants
[ +vowel ] -> [ +highTone ] / _CC#

#otherwise the second to last (penultimate) syllable stressed
[ +vowel ] -> [ +highTone ] / _CVC#

	'''],stressful=True
	))


Odden_Problems.append(Problem(
	u'''
Bukusu Odden 105
	''',
	[ 
	# Imperative	3pl pres		1sg pres		Gloss
	(u"ča",			u"βača",		u"ñǰa"),		# go
	(u"čexa",		u"βačexa",		u"ñǰexa"),		# laugh
	(u"čučuuŋga",	u"βačučuuŋga",	u"ñǰučuuŋga"),	# sieve
	(u"talaanda",	u"βatalaanda",	u"ndalaanda"),	# go around
	(u"teexa",		u"βateexa",		u"ndeexa"),		# cook
	(u"tiira",		u"βatiira",		u"ndiira"),		# get ahold of
	(u"piima",		u"βapiima",		u"mbiima"),		# weigh
	(u"pakala",		u"βapakala",	u"mbakala"),	# writhe in pain
	(u"ketulula",	u"βaketulula",	u"ŋgetulula"),	# pour out
	(u"kona",		u"βakona",		u"ŋgona"),		# pass the night
	(u"kula",		u"βakula",		u"ŋgula"),		# buy
	(u"kwa",		u"βakwa",		u"ŋgwa")		# fall 
	], 
	solutions = [u'''
stem
βa + stem
n + stem

        # Postnasal voicing
        [ -voice ] -> [ +voice ] / [ +nasal ] _
        # Nasal place assimilation
        # [ +nasal ] -> [ αplace ] / _ [αplace]
        [ +nasal ] -> place+1 / _ C
	''']
	))


Odden_Problems.append(Problem(
	u'''
Lithuanian Odden 114
	''',
	[ 
	# a.
	# /at/
	(u"at-eiti",None),		# to arrive
	(u"at-imti",None),		# to take away
	(u"at-nešti",None),		# to bring
	(u"at-leisti",None),	# to forgive
	(u"at-likti",None),		# to complete
	(u"at-ko:pti",None),	# to rise
	(u"at-praši:ti",None),	# to ask
	(u"at-kurti",None),		# to reestablish

	# /ap/
	(None,u"ap-eiti"),		# to circumvent
	(None,u"ap-ieško:ti"),	# to search everywhere
	(None,u"ap-akti"),		# to become blind
	(None,u"ap-mo:ki:ti"),	# to train
	(None,u"ap-temdi:ti"),	# to obscure
	(None,u"ap-šaukti"),	# to proclaim

	# b.
	# /at/
	(u"ad-bekti",None),		# to run up
	(u"ad-gauti",None),		# to get back
	(u"ad-bukti",None),		# to become blunt
	(u"ad-gimti",None),		# to be born again

	# /ap/
	(None,u"ab-gauti"),		# to deceive
	(None,u"ab-ž^yureti"),	# to have a look at
	(None,u"ab-želti"),		# to become overgrown
	(None,u"ab-dauži:ti"),	# to damage
	(None,u"ab-draski:ti"),	# to tear


	], 
	solutions = [u'''
at + stem
ap + stem

# Voicing assimilation
[ -sonorant ] -> [ +voice ] / _ [ -sonorant +voice ]
	''']
	))


Odden_Problems.append(Problem(
	u'''
Armenian Odden 116
	''',
	[ 
	# a.
	(u"kert^ham",),			# I will go
	(u"k-asiem",),			# I will say
	(u"k-aniem",),			# I will do
	(u"k-akaniem",),		# I will watch
	(u"k-oxniem",),			# I will bless
	(u"k-urriem",),			# I will swell

	# b.
	(u"kə-tam",),			# I will give
	(u"kə-kienam",),		# I will exist
	(u"gə-bəzzam",),		# I will buzz
	(u"gə-lam",),			# I will cry
	(u"gə-zəram",),			# I will bray
	(u"k^hə-t^huoyniem",),	# I will allow
	(u"k^hə-č^hap^hiem",),	# I will measure
	(u"g^hə-b^hieřiem",),	# I will carry
	(u"g^hə-g^huom",),		# I will come
	(u"g^hə-d^z^hieviem",),	# I will form
	], 
	solutions = [u'''
at + stem
ap + stem

# Voicing assimilation
[ -sonorant ] -> [ +voice ] / _ [ +sonorant +voice ]
	''']
	))




Odden_Problems.append(Problem(
	u'''
Yawelmani Odden 170
	''',
	[
	# Nonefuture	Imperative	Dubitative	Passive_aorist	Gloss 

	(u"xathin",		u"xatk'a",	u"xatal",	u"xatit"),		# eat
	(u"dubhun",		u"dubk'a",	u"dubal",	u"dubut"),		# lead by hand
	(u"xilhin",		u"xilk'a",	u"xilal",	u"xilit"),		# tangle
	(u"k'oʔhin",	u"k'oʔk'o",	u"k'oʔol",	u"k'oʔit"),		# throw
	(u"doshin",		u"dosk'o",	u"do:sol",	u"do:sit"),		# report
	(u"ṣaphin",		u"ṣapk'a",	u"ṣa:pal",	u"ṣa:pit"),		# burn
	(u"lanhin",		u"lank'a",	u"la:nal",	u"la:nit"),		# hear
	(u"mek'hin",	u"mek'k'a",	u"me:k'al",	u"me:k'it"),	# swallow
	(u"wonhin",		u"wonk'o",	u"wo:nol",	u"wo:nit"),		# hide

	(u"p'axathin",	u"p'axatk'a",	u"p'axa:tal",	u"p'axa:tit"),	# mourn
	(u"hiwethin",	u"hiwetk'a",	u"hiwe:tal",	u"hiwe:tit"),	# walk
	(u"ʔopothin",	u"ʔopotk'o",	u"ʔopo:tol",	u"ʔopo:tit"),	# arise from bed
	(u"yawalhin",	u"yawalk'a",	u"yawa:lal",	u"yawa:lit"),	# follow
	(u"paʔiṭhin",	u"paʔiṭk'a",	u"paʔṭal",		u"paʔṭit"),		# fight
	(u"ʔilikhin",	u"ʔilikk'a",	u"ʔilkal",		u"ʔilkit"),		# sing
	(u"logiwhin",	u"logiwk'a",	u"logwol",		u"logwit"),		# pulverize
	(u"ʔugunhun",	u"ʔugunk'a",	u"ʔugnal",		u"ʔugnut"),		# drink
	(u"lihimhin",	u"lihimk'a",	u"lihmal",		u"lihmit"),		# run
	(u"ʔayiyhin",	u"ʔayiyk'a",	u"ʔayyal",		u"ʔayyit"),		# pole a boat
	(u"t'oyixhin",	u"t'oyixk'a",	u"t'oyxol",		u"t'oyxit"),	# give medicine
	(u"luk'ulhun",	u"luk'ulk'a",	u"luk'lal",		u"luk'lut"),	# bury
	(u"so:nilhin",	u"so:nilk'a",	u"sonlol",		u"sonlit"),		# put on back
	(u"ʔa:milhin",	u"ʔa:milk'a",	u"ʔamlal",		u"ʔamlit"),		# help
	(u"mo:yinhin",	u"mo:yink'a",	u"moynol",		u"moynit"),		# become tired
	(u"ṣa:lik'hin",	u"ṣa:lik'k'a",	u"ṣalk'al",		u"ṣalk'it")		# wake up
	], 
	solutions = [u'''
stem + hin/hun
stem + k'a/k'o
stem + al/ol
stem + it/ut

# Vowel Harmony
[ +vowel αhi ] -> [ +round ] / [ +vowel αhi +round ]

# Vowel Shortening
[ +vowel ] -> [ -long ] / _CC

# Epenthesis OR Vowel Deletion (One or the other - Both Works with the data)
0 -> [ +vowel +high ] / C_CC    # Epenthesis
[ +vowel -long ] -> 0 / VC_CV    # Vowel Deletion
	''']
	))


# Halle's Problem Book in Phonology
Halle_Problems = []



Problem('''
Indonesian Halle 125
''',
[
   # simple form        prefixed form        gloss
     (u"lempar",        u"məlempar"),       #'throw'
     (u"rasa",          u"mərasa"),         #'feel'
     (u"wakil",         u"məwakili"),       #'represent'
     (u"yakin",         u"məyakini"),       #'convince'
     (u"masak",         u"məmasak"),        #'cook'
     (u"nikah",         u"mənikah"),        #'marry'
     (u"ŋaco",          u"məŋaco"),         #'chat'
     (u"ɲaɲi",          u"məɲaɲi"),         #'sing'
     (u"hituŋ",         u"məŋhituŋ"),       #'count'
     (u"gambar",        u"məŋgambar"),      #'draw a picture'
     (u"kirim",         u"məŋirim"),        #'send'
     (u"dəŋar",         u"məndəŋar"),       #'hear'
     (u"tulis",         u"mənulis"),        #'write'
     (u"bantu",         u"məmbantu"),       #'help'
     (u"pukul",         u"məmukul"),        #'hit'
     (u"ǰahit",         u"mən̆ǰahit"),       #'sew'
     (u"čatat",         u"mən̆čatat"),       #'note down'
     (u"ambil",         u"məŋambil"),       #'take'
     (u"isi",           u"məŋisi"),         #'fill up'
     (u"undaŋ",         u"məŋundaŋ"),       #'invite'
],
solutions=[u'''
stem
mə + stem + i
ŋ > 0 / #_C
[-sonorant] > [+nasal] / #mə_
[+nasal] > place+1 / _ [-vowel]
i > 0 / m [-glide]* _ #
''',
#            u'''
# stem
# mə + stem
# ŋ > ∅ / __ C, [+sonorant] 
# ŋ > m / __ [-sonorant, LAB]
# ŋ > n / __ [-sonorant, +ant]
# ŋ > ɲ/ __ [-sonorant, -ant]
# [-vce, -cont] > ∅ / [+nasal] __ across a morpheme boundary
# ''' 
])





# Roca's A Workbook in Phonology
Roca_Problems = []

Roca_Problems.append(Problem(
	u'''
German Roca 16
	''',
	[ 
	# lexical form		phonetic form	gloss

            # Uninflected/Plural/Infinitive/Masculine
	(u"tak", u"tagə",None,None),			# day
	(u"volk", u"volkə",None,None),			# people
	(u"pəriskop", u"pəriskopə",None,None),			# periscope
	(u"hof", u"höfə",None,None),			# courtyard
	(u"wək", u"wəgə",None,None),			# way
	    (u"ros", u"rosə",None,None), 			# horse
	(u"raup",None,u"raubən",			None),			# robbery
	(u"ləit",None,u"ləidən",None),			# sorry
	(u"lop",None,u"lobən",None),			# praise
	(u"lant",None,u"landən", 			None),			# land
	(u"rat",None,u"ratən",None),			# advice
	    (u"grəis",u"grəizes",None,None),			# old man
	(u"braf",None,None,u"bravər"),			# obedient (pred.) /  (masc.)
	], 
	solutions = [u'''
stem
stem + ə
stem + ən
stem + ər

[-sonorant] -> [-voice] / _#
	''']
	))



Roca_Problems.append(Problem(
	u'''
Dutch Roca 17
	''',
	[ 
	# lexical form		phonetic form	gloss
	(u"klaptə",),	# applauded
	(u"krabdə",),	# scratched
	(u"rɛdə",),		# saved
	(u"vɩstə",),		# fished
	(u"razdə",),		# raged
	(u"zɛtə",),		# put
	(u"maftə",),		# slept
	(u"klovdə",),	# split
	(u"lɛɣdə",),		# laid
	(u"laxtə",),		# laughed

	(u"rumdə",),		# praised
	(u"zundə",),		# kissed
	(u"meŋdə",),		# mixed
	(u"rurdə",),		# stirred
	(u"rɔldə",),		# rolled
	(u"ajdə",),		# caressed
	(u"skidə",)		# skied

	], 
	solutions = [u'''
stem + də
        [-sonorant] > [-voice] / [-voice] _
	''']
	))


Roca_Problems.append(Problem(
	u'''
Zoque Roca 25
	''',
	[ 
	# lexical_form		my+
	(u"pama", 			u"mbama"),			# clothing
	(u"tatah", 			u"ndatah"),			# father
	(u"kwarto", 		u"ŋgwarto"),			# room
	(u"plato", 			u"mblato"),			# plate
	(u"trama", 			u"ndrama"),			# trap
	(u"disko", 			u"ndisko"),			# record
	(u"gaju", 			u"ŋgaju"),			# rooster
	(u"čoʔngoja", 		u"ɲǰoʔngoja"),			# rabbit
	(u"tsima", 			u"ndzima"),			# calabash
	(u"sʌk", 			u"sʌk"),			# beans
	(u"faha", 			u"faha"),			# belt
	(u"šapun", 			u"šapun"),			# soap
	], 
	solutions = [
u'''
stem
ɲ + stem
        [+nasal] > 0 / #_[-sonorant +continuant -voice]
        [+nasal] > place+1 / #_ C
        C > [+voice] / #[+nasal]C*_
	''']
	))



Roca_Problems.append(Problem(
	u'''
Anxiang Roca 37
	''',
	[ 
	# base 		diminutive_form
	(u"tie",	u"tie tiər"),	# small dish, plate
	(u"mian",	u"mian miər"),	# face
	(u"tai",	u"tai tər"),	# belt
	(u"pau",	u"pau pər"),	# bud
	(u"ke",		u"ke kər"),		# check, chequer
	(u"fa",		u"fa fər"),		# law, way
	(u"o",		u"o ər"),		# bird's nest
	(u"ti",		u"ti tiər"),	# bamboo flute
	(u"tin",	u"tin tiər"),	# nail
	(u"p^hu",	u"p^hu p^hər"),	# spread
	(u"tx̯y",	u"tx̯y tx̯yər")	# pearl
	], 
	solutions = [u'''
# No solution
"""
stem
stem + partial_stem + ər

*** FIND THE PART OF THE BASE STEM IN THE DUPLICATED FORM
"""
	''']
	))


Roca_Problems.append(Problem(
	u'''
Verlan Roca 31
	''',
	[ 
	# French 		Verlan			gloss
	(u"gamɛ̃",		u"mɛ̃ga"),		# kid (masc.)
	(u"gamin",		u"minga"),		# kid (fem.)
	(u"kopɛ̃",		u"pɛ̃ko"),		# mate (masc.)
	(u"kopin",		u"pinko"),		# mate (fem.)
	(u"frãsɛ",		u"sɛfrã"),		# French (masc.)
	(u"frãsɛz",		u"sɛzfrã"),		# French (fem.)
	(u"fyme",		u"mefy"),		# to smoke
	(u"finir",		u"nirfi"),		# to finish

	(u"rigolo",		u"logori"),		# funny
	(u"tabure",		u"rebuta"),		# stool
	(u"papiyɔ̃", 	u"yɔ̃pipa"),		# butterfly

	(u"sigarɛt",	u"garɛtsi"),	# cigarette
	(u"korida",		u"ridako"),		# bull fight

	(u"ãkyle",		u"leãky"),		# sod
	(u"degölas",	u"lasdegö"),	# disgusting
	(u"karate",		u"tekara"),		# karate
	],
    supervised=True,
	solutions = [u'''
# No solution
# Syllable inversion
# disyllabic: first and second syllables switch places
# trisyllabic: ?
	''']
	))



Roca_Problems.append(Problem(
	u'''
Icelandic Roca 35
	''',
	[
            # y, in the IPa system, is ü in the APA system
	# Nom_sg Acc_sg Dat_sg Gen_sg Dat_pl Gen_pl gloss

	# Nom_sg	Acc_sg
	(u"dagur",	u"dag",		None, None, None, None),		# day
	(u"staður",	u"stað",	None, None, u"stöðum", None),		# place
	(u"hestur",	u"hest",	None, None, None, None),		# horse
	(u"bær",	u"bæ",		None, None, None, None),		# farmhouse
	(u"læknir",	u"lækni",	None, None, None, None),		# physician

	# Nom_sg	Dat_sg
	(u"lifur",	None,	u"lifri", None, None, None),	# liver
	(u"akur",	None,	u"agri", None, u"ökrum", None),		# field
	(u"aldur",	None, 	u"aldri", None, u"öldrum", None),	# age

	# Nom_sg	Acc_sg	Gen_sg	Dat_pl	Gen_pl
	(u"lüfur",	u"lüf",	None,	u"lüfs",	u"lüfjum",	u"lüfja"),	# medicine
	(u"bülur",	u"bül",	None,	u"büls",	u"büljum",	u"bülja"),	# snowstorm
	(u"söngur",	u"söng", None,	u"söngs",	u"söngvum",	u"söngva"),	# song

	# Nom_sg	Dat_pl
	(u"barn", None, None, None, u"börnum", None), # child
	(u"baggi", None, None, None, u"böggull", None), # package
	(u"jaki", None, None, None, u"jökull", None), # glacier
	(u"θagga", None, None, None, u"θögull", None), # taciturn
	(u"kalla", None, None, None, u"köllum", None), # call (1st pl.)
#	(u"akur", None, None, None, u"ökrum", None), # field
#	(u"aldur", None, None, None, u"öldrum", None), # age
#	(u"staður", None, None, None, u"stöðum", None) # place

	], 
	solutions = [u'''
stem + ur
stem
stem + ri
stem + s
stem + jum
stem + ja
        u > 0 / V _
        [-continuant -sonorant] > [+voice] / _ r
        
	''']
	))


Roca_Problems.append(Problem(
	u'''
Lumasaaba Roca 89
	''',
	[
	# a+[word]	small+[word]
	(u"iɲɉele", u"xaçele"),	# frog (ie. a frog, small frog)
	(u"iŋga:fu", u"xaxa:fu"), 	# cow
	(u"imbeβa",	u"xaβeβa"),		# rat
	(u"iŋgoxo",	u"xakoxo"),		# hen
	(u"iŋgwe",	u"xakwe"),		# leopard
	(u"indali",	u"xatali"),		# beer
	(u"imboko",	u"xaβoko")		# buffalo
	], 
	solutions = [u'''
# No solution
# iɲ/iŋ/in/im + stem
# xa + stem
# *** FIND THE STEM INITIAL CONSONANT VARIATION
im + stem
xa + stem
        C > [-continuant +voice] / [+nasal] _
        [+nasal] > place+1 / _ C
	''']
	))

Roca_Problems.append(Problem(
	u'''
Tunica Roca 104
According to:
http://pluto.huji.ac.il/~msyfalk/Phon/English/OrderHwk.pdf
there is a bug in this problem - the third singular feminine present progressive suffix should not have any stress markers
	''',
	[
	# Infinitive	3rd_sg_masc		3rd_sg_fem		3rd_sg_fem_pres_prog
	(u"pó", u"póʔuhki",	u"póʔɔki", u"póhkʔaki"),	# look
	(u"pí",	u"píʔuhki",	u"píʔɛki", u"píhkʔaki"),	# emerge
	(u"já", u"jáʔuhki", u"jáʔaki", u"jáhkʔaki"),	# do
	(u"čú", u"čúʔuhki", u"čúʔɔki", u"čúhkʔaki"),	# take

	(u"hára", u"hárʔuhki", u"hárʔaki", u"hárahkʔaki"),	# sing
	(u"hípu", u"hípʔuhki", u"hípʔɔki", u"hípuhkʔaki"),	# dance
	(u"náši", u"nášʔuhki", u"nášʔɛki", u"nášihkʔaki")	# lead someone
	], 
	solutions = [u'''
# No solution
stem
stem + ʔuhki
stem + ʔaki
stem + hkʔaki
        a > ɔ / [+rounded] C _
        a > ɛ / [+vowel +high] C _
        [+vowel -highTone] > 0 / _ʔ
	'''],
    stressful=True
    
	))



Halle_Problems.append(Problem('''
Turkish Halle 85
	''',
	[
	# Nom_sg 	Gen_sg 		Nom_pl 		Gen_pl 		gloss
	(u"ip", u"ipin", u"ipler", u"iplerin"), 		# rope
	(u"kɨz", u"kɨzɨn", u"kɨzlar", u"kɨzlarɨn"),		# girl
	(u"yüz", u"yüzün", u"yüzler", u"yüzlerin"),		# face
	(u"pul", u"pulun", u"pullar", u"pullarɨn"),		# stamp
	(u"el", u"elin", u"eller", u"ellerin"), 		# hand
	(u"čan", u"čanɨn", u"čanlar", u"čanlarɨn"), 	# bell
	(u"köy", u"köyün", u"köyler", u"köylerin"), 	# village
	(u"son", u"sonun", u"sonlar", u"sonlarɨn") 		# end
	],
	solutions = [u'''
# solution found by system
stem
stem + un
stem + lar
stem + larɨn
        V > [-back -low] / [+vowel -back] [ ] _
        V > [-rounded] / [ -rounded ] [ ]* _
	''']
	))

Halle_Problems.append(Problem('''
Turkish Halle 97
	''',
	[
	# noun_stem		possessed_form		gloss
	(u"ip", u"ipi"),		# rope
	(u"bit", u"biti"),		# louse
	(u"sebep", u"sebebi"),	# reason
	(u"kanat", u"kanadɨ"),	# wing
	(u"šeref", u"šerefi"),	# honor
	(u"kɨč", u"kɨčɨ"),		# rump
	(u"pilot", u"pilotu"),	# pilot
	(u"demet", u"demeti"),	# bunch
	(u"šarap", u"šarabɨ"),	# wine
	(u"ahmet", u"ahmedi"),	# Ahmed
	(u"pabuč", u"pabuǰu"),	# slipper
	(u"güč", u"güǰü"),		# power
	(u"sepet", u"sepeti"),	# basket
	(u"sanat", u"sanatɨ"),	# art
	(u"kep", u"kepi"),		# cap
	(u"kurt", u"kurdu"),	# worm
	(u"sač", u"sačɨ"),		# hair
	(u"renk", u"rengi")		# color
	],
	solutions = [u'''
# No solution
stem
stem + in/ɨn/ün/un
stem + ler/lar
stem + ler/lar + in/ɨn

	''']
	))

Halle_Problems.append(Problem('''
Russian Halle 109
	''',
	[
	# from 		without		next_to
	(u"at rózɨ", u"b^yiz rózɨ", u"u rózɨ"),	# rose
	(u"at álɨ", u"b^yiz álɨ", u"u álɨ"),	# Ala (name)
	(u"at karóvɨ", u"b^yiz karóvɨ", u"u karóvɨ"),	# cow
	(u"ad baradɨ́", u"b^yiz baradɨ́", u"u baradɨ́"),	# beard
	(u"at s^yistrɨ́", u"b^yis s^yistrɨ́", u"u s^yistrɨ́")	# sister
	],
	solutions = [u'''
# No solution
# Voicing Assimilation - consonant alternations in the preposition

	'''],stressful=True
	))



Halle_Problems.append(Problem('''
Klamath Halle 113
	''',
	[
	# underlying	surface
	(u"honli:na",	u"holli:na"), # flies along the bank
#	(u"honl̥y",		u"holhi"), # flies into
            (u"honl̥",		u"holh"), # flies into
	(u"honl`a:l`a",	u"holʔa:l`a"), # flies into the fire
	(u"pa:ll̥a",		u"pa:lha"), # dries on
	(u"yalyall`i",	u"yalyalʔi") # clear
	],
	solutions = [u'''
        n > l / [+lateral] _
        l̥ > h / l _
        l` > ʔ / l _
	'''],
                              supervised=True
	))


Halle_Problems.append(Problem('''
Russian Halle 115
	''',
	[
	# 1st_sg_pres	past_masc	past_fem	past_pl	

	(u"v^yirnú", u"v^yirnúl", u"v^yirnúla", u"v^yirnúl^yi"), # return (s. th.)
	(u"vrú", u"vrál", u"vralá", u"vrál^yi"), # lie, mislead
	(u"stayú", u"stayál", u"stayála", u"stayál^yi"), # stand

	(u"p^yikú", u"p^yók", u"p^yiklá", u"p^yikl^yí"), # bake (ie. whether he baked, were he to bake)
	(u"v^yizú", u"v^yós", u"v^yizlá", u"v^yizl^yí"), # transport (ie. whether he carried, were he to carry)
	(u"magú", u"mók", u"maglá", u"magl^yí"), # can (ie. whether he could, were he to be able)
	(u"móknu", u"mók", u"mókla", u"mókl^yi"), # soak (ie. whether he soaked, where he to soak)


	],
	solutions = [u'''
# No solution

	'''],
                              stressful=True
	))


Halle_Problems.append(Problem('''
Russian Halle 149
	''',
	[
	# Nom_sg 	Gen_pl	Dat_sg	Nom_pl	gloss
	(u"luná", u"lún", u"lun^yɛ́", u"lúnɨ"), # moon
	(u"dɨrá", u"dɨ́r", u"dɨr^yɛ́", u"dɨ́rɨ"), # hole
	(u"travá", u"tráf", u"trav^yɛ́", u"trávɨ"), # grass

	(u"p^yilá", u"p^yíl", u"p^yil^yɛ́", u"p^yílɨ"), # saw
	(u"valná", u"vóln", u"valn^yɛ́", u"vólnɨ"), # wave
	(u"galavá", u"galóf", u"galav^yɛ́", u"gólavɨ"), # head

	(u"žɨl^yizá", u"žɨl^yós", u"žɨl^yiz^yɛ́", u"žél^yizɨ"), # gland
	(u"žɨná", u"žón", u"žɨn^yɛ́", u"žónɨ"), # wife
	(u"zm^yiyá", u"zm^yéy", u"zm^yiyɛ́", u"zm^yéyi"), # snake

	(u"m^yɛ́na", u"m^yɛ́n", u"m^yén^yi", u"m^yɛ́nɨ"), # change
	(u"p^yil^yiná", u"p^yil^yón", u"p^yil^yin^yɛ́", u"p^yil^yinɨ́"), # shroud
	(u"b^yis^yɛ́da", u"b^yis^yɛ́t", u"b^yis^yéd^yi", u"b^yis^yɛ́dɨ"), # conversation

	(u"b^yidá", u"b^yɛ́t", u"b^yid^yɛ́", u"b^yɛ́dɨ"), # sorrow
	(u"p^yitá", u"p^yát", u"p^yit^yɛ́", u"p^yitɨ́"), # heel
	(u"st^yiná", u"st^yɛ́n", u"st^yin^yɛ́", u"st^yɛ́nɨ"), # wall

	(u"r^yiká", u"r^yɛ́k", u"r^yik^yɛ́", u"r^yék^yi"), # river
	(u"slugá", u"slúk", u"slug^yɛ́", u"slúg^yi"), # servant
	(u"blaxá", u"blóx", u"blax^yɛ́", u"blóx^yi") # flea
	],
	solutions = [u'''
stem + á
stem
stem + ɛ́
stem + ɨ
        [-sonorant] > [-voice] / _ #
        C > [+palletized] / _ ɛ́
        V > [-highTone] / _ C* [+highTone]

	'''], stressful=True
	))


Halle_Problems.append(Problem('''
Sao Tome Creole Halle 141
	''',
	[
	# Portuguese	Sao_Tome_Creole
	(u"vešpʌ", u"vešpa"), # wasp
	(u"šigar", u"šiga"), # to arrive
	(u"sɛgu", u"sɛgu"), # blind
	(u"šumbu", u"sumbu"), # lead
	(u"pɜškar", u"piška"), # to fish
	(u"r̃atu", u"latu"), # rat
	(u"artɜ", u"ači"), # art
	(u"tašu", u"tasu"), # pan
	(u"kulpʌ", u"klupa"), # blame
	(u"r̃ɜšpʌitu", u"lišpetu"), # courtesy
	(u"ʌguʎʌ", u"guya"), # needle
	(u"tirar", u"čila"), # to take out
	(u"dyabu", u"ǰabu"), # devil
	(u"šʌmar", u"sama"), # to call
	(u"kwazɜ", u"kwaži"), # almost
	(u"tardɜ", u"taǰi"), # afternoon
	(u"idadɜ", u"daǰi"), # age
	(u"kʌprišu", u"kaplisu"), # caprice
	(u"fɛr̃u", u"fɛlu"), # iron
	(u"brõzɜ", u"blõzi"), # bronze
	(u"fižir", u"fiži"), # to pretend
	(u"žemʌ", u"zema"), # egg yolk
	(u"diʌ", u"ǰa"), # day
	(u"forsa", u"fosa"), # strength
	(u"mɔrtɜ", u"mɔči"), # death
	(u"pulgʌ", u"pluga"), # flea
	(u"bišu", u"bisu"), # animal
	(u"pɜdir", u"piǰi"), # to ask
	(u"tiʌ", u"ča"), # aunt
	(u"kʌižu", u"kezu"), # cheese
	(u"pʌlasyu", u"palašu"), # place
	(u"bʌrbʌiru", u"blabelu"), # barber
	(u"ifɛr̃nu", u"fɛnu"), # hell
	(u"sinku", u"šinku") # five

	], supervised=True,
	solutions = [u'''
# No solution

	''']
	))



Halle_Problems.append(Problem('''
Swahili Halle 133
	''',
	[
	# singular	Plural_option1	plural_option2 		gloss
	(u"ubale", u"m̩bale", None),		# piece
	(u"udago", u"n̩dago", None),		# nut-grass
	(u"ugimbi", u"ŋ̩gimbi", None),		# beer
	(u"uǰia", u"ɲ̩ǰia", None),		# passage-way
	(u"upaǰa", u"p^haǰa", u"mapaǰa"),		# a bulging
	(u"upamba", u"p^hamba", None),		# (type of) knife
	(u"utunzo", u"t^hunzo", u"matunzo"),		# guardianship
	(u"utunda", u"t^hunda", None),		# string of beads
	(u"ukelele", u"k^helele", u"makelele"), 	# a cry
	(u"ukumbi", u"k^humbi", None),		# porch
	(u"učoma", u"č^homa", u"mačoma"),		# a burning
	(u"učaŋgo", u"č^haŋgo", None),		# small intestine
	(u"ufuasi", u"fuasi", u"mafuasi"),		# imitation
	(u"ufuko", u"fuko", None),		# sea-shore
	(u"uvušo", u"vušo", u"mavušo"),		# a ferrying
	(u"uvumbi", u"vumbi", None),		# speck of dust
	(u"usiku", u"siku", u"masiku"),		# night
	(u"usira", u"sira", None),		# (type of) powder
	(u"ušono", u"šono", u"mašono"),		# sewing
	(u"ušaŋga", u"šaŋga", None),		# bead
	(u"uwiŋgu", u"m̩biŋgu", None),		# sky, heaven
	(u"uwili", u"m̩bili", None),		# duality
	(u"ulimi", u"n̩dimi", None),		# tongue
	(u"urefu", u"n̩defu", None),		# length, distance
	(u"umio", u"mio", None),		# throat
	(u"wimbo", u"ɲimbo", None),		# song
	(u"wembe", u"ɲembe", None),		# razor
	(u"wakati", u"ɲakati", None),		# time
	(u"uši", u"ɲuši", None),		# eyebrow
	(u"šoka", None, u"mašoka"),		# axe
	(u"tunda", None, u"matunda"),		# fruit
	(u"kaša", None, u"makaša")		# safe
	],
	solutions = [u'''
u + stem
m̩ + stem
ma + stem
        [+nasal] > 0 / _[+aspirated]
        [+aspirated] > [-aspirated] / [ ] _
        [+nasal] > place+1 / #_C
	''']
	))


# Problem('''
# Child Language Halle 117
# ''',
# [
#    # child word        adult word
#      (u"puppy",        u"pəʔiy"),
#      (u"kick",          u"kɩʔ"),
#      (u"beyʔiü",       u"baby"),
#      (u"wɑkt",         u"walks"),
#      (u"wɑkt",         u"walked"),
#      (u"rənd",         u"ran"),
#      (u"mænd",         u"men"),
#      (u"pɛt",          u"pet"),
#      (u"kænd",         u"can"),
#      (u"dɩʔ",          u"did"),
#      (u"dəd",          u"does"),
#      (u"tɑkt",         u"talks"),
#      (u"biyt",         u"beat"),
#      (u"dayʔ",         u"died"),
#      (u"teykiʔ/tuk",   u"took"),
#      (u"bɩt",          u"bit"),
#      (u"tɑkɨʔ",        u"talked"),
#      (u"dæʔiy",        u"daddy"),
#      (u"bɑʔiy",        u"Bobby"),
#      (u"tæg",          u"tag"),
#      (u"peyʔər",       u"paper"),
#      (u"teykt",        u"takes"),
#      (u"dɑgd",         u"dogs"),
#      (u"tuwʔ",         u"toot"),
#      (u"tuwt",         u"suit"),
#      (u"keyʔ",         u"cake")
# ], supervised=True,
# solutions=[u'''

# ''' 
# ])


Problem('''
    Ewe Halle 49
    ''',
    [
       # data              gloss
         u"zrɔ̃",           #'to be smooth'
         u"ñra",           #'to rage'
         u"lɔ̃",            #'to love'
         u"kpla",          #'to intertwine'
         u"mlagoo",        #'thick'
         u"gblaa",         #'wide'
         u"lolo",          #'to be large'
         u"wlu",           #'to dig'
         u"β|la",           #'suddenly'
         u"srɔ̃",           #'wife'
         u"lãkle",         #'leopard'
         u"hle",           #'to spread out'
         u"vlɔ",           #'to go far away'
         u"atra",          #'mangrove'
         u"dru",           #'to be bent'
         u"fle",           #'to pluck'
         u"glamaa",        #'uneven'
         u"litsa",         #'chameleon'
         u"dzre",          #'to quarrel'
         u"ɣla",           #'to hide'
         u"xloloo",        #'rough'
         u"tsro",          #'bark' (of tree)
         u"φ|le",           #'to buy'
         u"blema",         #'formerly'
         u"dɔlele",        #'illness'
         u"ŋlɔ",           #'to write'
         u"yre",           #'evil'
         u"adoglo",        #'lizard'
         u"kplu",          #'jug'
         u"kpali",         #'Paris'
         u"klalo",         #'finished'
         u"atrakpoe",      #'steps'
    ],
    solutions=[u'''
    r --> l  / [-COR] __  
    r --> l / #__ 
    '''
    ],
    parameters={"type": "alternation", "alternations": [{u"l":u"r"}]})

Problem('''
    Ganda Halle 51
    ''',
    [
       # data              gloss
         u"kola",          #'do'
         u"lwana",         #'fight'
         u"buulira",       #'tell'
         u"lja",           #'eat'
         u"luula",         #'sit'
         u"omugole",       #'bride'
         u"lumonde",       #'sweet potato'
         u"eddwaliro",     #'hospital'
         u"oluganda",      #'Ganda language'
         u"olulimi",       #'tongue'
         u"wulira",        #'hear'
         u"beera",         #'help'
         u"jjukira",       #'remember'
         u"erjato",        #'canoe'
         u"omuliro",       #'fire'
         u"effirimbi",     #'whistle'
         u"emmeeri",       #'ship'
         u"eraddu",        #'lightning'
         u"wawaabira",     #'accuse'
         u"lagira",        #'command'
         u"ebendera",      #'flag'
         u"leerwe",        #'railwaj'
         u"luula",         #'ruler'
         u"ssaffaali",     #'safari'
    ],
    solutions=[u'''
    l --> r  / V,[+high, -back] __  
    '''],
    parameters={"type": "alternation", "alternations": [{u"l":u"r"}]})

Problem('''
Japanese Halle 127
''',
[
   # present     negative     volitional   past       inchoative     gloss
     (u"neru",   u"nenai",    u"netai",    u"neta",   u"neyoo"),     #'sleep'
     (u"miru",   u"minai",    u"mitai",    u"mita",   u"miyoo"),     #'see'
     (u"šinu",   u"šinanai",  u"šinitai",  u"šinda",  u"šinoo"),     #'die'
     (u"yomu",   u"yomanai",  u"yomitai",  u"yonda",  u"yomoo"),     #'read'
     (u"yobu",   u"yobanai",  u"yobitai",  u"yonda",  u"yoboo"),     #'call'
     (u"kat^su", u"katanai",  u"kačitai",  u"katta",  u"katoo"),     #'win'
     (u"kasu",   u"kasanai",  u"kašitai",  u"kašita", u"kasoo"),     #'lend'
     (u"waku",   u"wakanai",  u"wakitai",  u"waita",  u"wakoo"),     #'boil'
     (u"t^sugu", u"t^suganai",u"t^sugitai",u"t^suida",u"t^sugoo"),   #'pour'
     (u"karu",   u"karanai",  u"karitai",  u"katta",  u"karoo"),     #'shear'
     (u"kau",    u"kawanai",  u"kaitai",   u"katta",  u"kaoo"),      #'buy'
     
],
solutions=[u'''
stem + ru
stem + anai
stem + itai
stem + ta
stem + yoo
t > d / [+voice -vowel]
r > 0 / {n,s,r,w,t} _

'''])

Problem('''
Mohawk Halle 121
''',
[
   # UR                       surface form          gloss
     (u"hranyahesʌ̃s",       u"ranahé:zʌ̃s"),       #'he trusts her'
     (u"hraketas",          u"ragé:das"),         #'he scrapes'
     (u"waʔhraketʔ",       u"wahá:gedeʔ"),       #'he scraped'
     (u"owisʔ",             u"ó:wizeʔ"),          #'ice, glass'
    # only stress
     (u"wakenuhweʔuneʔ",   u"wagenuhweʔú:neʔ"),  #'I had liked it'
     (u"ʌ̃khʌ̃teʔ",          u"ʌ̃khʌ̃́:deʔ"),         #'I shall go ahead'
    # bunch of stuff
     (u"yaknirʌ̃notʔ",    u"yagenirɔ́:nodeʔ"),   #'we two (exclusive) 
                                                    #are singing'
     (u"yakniehyaraʔs",   u"yagenehyá:raʔs"),   #'we two (exclusive)'
                                                    #remember'
     (u"yakwarʌ̃notʔ",    u"yagwarɔ́:nodeʔ"),    #'we (plural exlusive)
                                                    #are singing
     (u"yakwaehyaraʔs",   u"yagwehyá:raʔs"),    #'we (plural exclusive)
                                                    #remember 
     (u"hrayʌ̃thos",         u"rayʌ̃́thos"),         #'he plants'
     (u"hraehyaraʔs",       u"rehyá:raʔs"),       #'he remembers'
     (u"yekhreks",         u"yékreks"),          #'I push it'
     (u"yeʌ̃khrekʔ",        u"yɔ́kregeʔ"),         #'I will push it'
], supervised=True,
solutions=[u'''
h > 0 / # _
∅ --> e / [-sonorant] __ ʔ in the final syllable 
'''
])


Problem('''
Mohawk Halle 59
''',
[
   # data              gloss
     u"oli:deʔ",       #'pigeon'
     u"zahset",        #'hide it!' (sg.)
     u"ga:lis",        #'stocking'
     u"odahsa",        #'tail'
     u"wisk",          #'five'
     u"degeni",        #'two'
     u"aplam",         #'Abram, Abraham'
     u"oya:gala",      #'shirt'
     u"ohyotsah",      #'chin'
     u"labahbet",      #'catfish'
     u"sdu:ha",        #'a little bit'
     u"ǰiks",          #'fly'
     u"desdaʔn̥",       #'stand up!' (sg.)
     u"de:zeknw̥",      #'pick it up' (s.g)
],
            parameters={"type": "alternation",
             "alternations": [{u"b": u"p",
                               u"d": u"t",
                               u"g": u"k"}]},
solutions=[u'''
  / V,[+high, -back] __  
''',
])

Problem('''
Papago Halle 53
''',
[
   # data              gloss
     u"bíǰim",         #'turn around'
     u"tá:pan",        #'split'
     u"hídoḍ",         #'cook'
     u"čɨ́kid",         #'vaccinate'
     u"gátwid",        #'shoot'
     u"čúku",          #'become black'
     u"dágṣp",         #'press with hand'
     u"tóha",          #'become white'
     u"ǰú:kǐ",         #'rain' (noun)
     u"hɨ́wgid",        #'smell'
     u"číhaŋ",         #'hire'
     u"tóñi",          #'become hot'
     u"wíḍut",         #'swing'
     u"tá:taḍ",        #'feet'
     u"kí:čud",        #'build a house for'
     u"dó:dom",        #'copulate'
     u"tá:tam",        #'touch'
],
            parameters={"type": "alternation",
             "alternations": [{u"t": u"č",
                               u"d": u"ǰ"}]},
solutions=[u'''
t --> č / __ V,[+high] 
d --> ǰ / __ V,[+high]
'''])
           
Problem('''
Proto-Bantu Halle 55
''',
[
   # data              gloss
     u"βale",          #'two'
     u"leme",          #'tongue'
     u"taβe",          #'twig'
     u"pala",          #'antelope'
     u"kondɛ",         #'bean'
     u"zɔŋgɔ",         #'gall'
     u"βɛɣa",          #'monkey'
     u"βɛmbe",         #'pigeon'
     u"limo",          #'god, spirit'
     u"kaŋga",         #'guinea fowl'
     u"ɣɔmbɛ",         #'cattle'
     u"lelɔ",          #'fire'
     u"kiɣa",          #'eyebrow'
     u"ɣiɣɛ",          #'locust'
     u"kulu",          #'tortoise'
     u"oŋgo",          #'cooking pot'
     u"tɛndɛ",         #'palm tree'
     u"zala",          #'hunger'
     u"zɔɣu",          #'elephant'
     u"βele",          #'body'
     u"lɛlu",          #'chin, beard'
     u"eɣi",           #'water'
     u"kiŋgɔ",         #'neck'
     u"nto",           #'person'
],
solutions=[u'''
β --> b / C,[+nasal] __ 
l --> d / C,[+nasal] __ 
ɣ --> g / C,[+nasal] __
'''
],
parameters={"type": "alternation", "alternations": [{u"b": u"β",
                                          u"d": u"l",
                                          u"g": u"ɣ"}]})

Problem('''
Yokuts Halle 153
''',
[
   # aorist passive          aorist          future passive      gloss
     (u"xatit",              u"xathin",      u"xatnit"),         #'eat'
     (u"gopit",              u"gophin",      u"gopnit"),         #'take care of
                                                                 #an infant'
     (u"giyit",              u"giyhin",      u"giynit"),         #'touch'
     (u"mutut",              u"muthun",      u"mutnut"),         #'swear'
     (u"sa:pit",             u"saphin",      u"sapnit"),         #'burn'
     (u"go:bit",             u"gobhin",      u"gobnit"),         #'take in'
     (u"me:kit",             u"mekhin",      u"meknit"),         #'swallow'
     (u"ʔo:tut",             u"ʔothun",      u"ʔotnut"),         #'steal'
     (u"panat",              u"pana:hin",    u"pana:nit"),       #'arrive'
     (u"hoyot",              u"hoyo:hin",    u"hoyo:nit"),       #'name'
     (u"ʔilet",              u"ʔile:hin",    u"ʔile:nit"),       #'fan'
     (u"cuyot",              u"cuyo:hun",    u"cuyo:nut"),       #'urinate'
     (u"paxa:tit",           u"paxathin",    u"paxatnit"),       #'mourn'
     (u"ʔopo:tit",           u"ʔopothin",    u"ʔopotnit"),       #'arise from
                                                                 #bed'
     (u"hibe:yit",           u"hibeyhin",    u"hibeynit"),       #'bring water'
     (u"sudo:kut",           u"sudokhun",    u"sudoknut"),       #'remove'
],
solutions=[u'''

''' 
])
