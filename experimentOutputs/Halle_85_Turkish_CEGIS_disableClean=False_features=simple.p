(iresult
Result
p1
(dp2
S'startTime'
p3
F1565820514.2200551
sS'solutionSequence'
p4
(lp5
(ccopy_reg
_reconstructor
p6
(csolution
Solution
p7
c__builtin__
object
p8
NtRp9
(dp10
S'rules'
p11
(lp12
(irule
Rule
p13
(dp14
S'leftTriggers'
p15
(irule
Guard
p16
(dp17
S'endOfString'
p18
I00
sS'specifications'
p19
(lp20
(irule
FeatureMatrix
p21
(dp22
S'featuresAndPolarities'
p23
(lp24
sS'representation'
p25
V[  ]
p26
sba(irule
FeatureMatrix
p27
(dp28
g23
(lp29
(I01
S'bilabial'
p30
tp31
asg25
V[ +bilabial ]
p32
sbasS'optionalEnding'
p33
I00
sg25
V[ +bilabial ] [  ]*
p34
sS'starred'
p35
I01
sS'side'
p36
S'L'
sbsS'structuralChange'
p37
(irule
ConstantPhoneme
p38
(dp39
S'p'
Ve
sbsS'rightTriggers'
p40
(irule
Guard
p41
(dp42
g18
I00
sg19
(lp43
sg33
I00
sg25
V
sg35
I00
sg36
S'R'
sbsS'focus'
p44
(irule
FeatureMatrix
p45
(dp46
g23
(lp47
(I01
S'central'
p48
tp49
asg25
V[ +central ]
p50
sbsg25
V[ +central ] ---> e / [ +bilabial ] [  ]* _ 
p51
sba(irule
Rule
p52
(dp53
g15
(irule
Guard
p54
(dp55
g18
I00
sg19
(lp56
sg33
I00
sg25
V
sg35
I00
sg36
S'L'
sbsg37
(irule
ConstantPhoneme
p57
(dp58
S'p'
Vi
sbsg40
(irule
Guard
p59
(dp60
g18
I00
sg19
(lp61
(irule
FeatureMatrix
p62
(dp63
g23
(lp64
(I00
S'retroflex'
p65
tp66
asg25
V[ -retroflex ]
p67
sbasg33
I00
sg25
g67
sg35
I00
sg36
S'R'
sbsg44
(irule
ConstantPhoneme
p68
(dp69
S'p'
Ve
sbsg25
Ve ---> i /  _ [ -retroflex ]
p70
sbasS'prefixes'
p71
(lp72
(imorph
Morph
p73
(dp74
S'phonemes'
p75
(lp76
sba(imorph
Morph
p77
(dp78
g75
(lp79
sba(imorph
Morph
p80
(dp81
g75
(lp82
sba(imorph
Morph
p83
(dp84
g75
(lp85
sbasS'underlyingForms'
p86
(dp87
((imorph
Morph
p88
(dp89
g75
(lp90
Vi
aVp
asb(imorph
Morph
p91
(dp92
g75
(lp93
Vi
aVp
aVi
aVn
asb(imorph
Morph
p94
(dp95
g75
(lp96
Vi
aVp
aVl
aVe
aVr
asb(imorph
Morph
p97
(dp98
g75
(lp99
Vi
aVp
aVl
aVe
aVr
aVi
aVn
asbtp100
(imorph
Morph
p101
(dp102
g75
(lp103
Ve
aVp
asbs((imorph
Morph
(dp104
g75
(lp105
Vc\u030c
p106
aVa
aVn
asb(imorph
Morph
(dp107
g75
(lp108
Vc\u030c
p109
aVa
aVn
aV\u0268
aVn
asb(imorph
Morph
(dp110
g75
(lp111
Vc\u030c
p112
aVa
aVn
aVl
aVa
aVr
asb(imorph
Morph
(dp113
g75
(lp114
Vc\u030c
p115
aVa
aVn
aVl
aVa
aVr
aV\u0268
aVn
asbtp116
(imorph
Morph
p117
(dp118
g75
(lp119
Vc\u030c
p120
aVa
aVn
asbs((imorph
Morph
p121
(dp122
g75
(lp123
Vk
aV\u0268
aVz
asb(imorph
Morph
p124
(dp125
g75
(lp126
Vk
aV\u0268
aVz
aV\u0268
aVn
asb(imorph
Morph
p127
(dp128
g75
(lp129
Vk
aV\u0268
aVz
aVl
aVa
aVr
asb(imorph
Morph
p130
(dp131
g75
(lp132
Vk
aV\u0268
aVz
aVl
aVa
aVr
aV\u0268
aVn
asbtp133
(imorph
Morph
p134
(dp135
g75
(lp136
Vk
aV\u0268
aVz
asbssS'suffixes'
p137
(lp138
(imorph
Morph
p139
(dp140
g75
(lp141
sba(imorph
Morph
p142
(dp143
g75
(lp144
V\u0268
aVn
asba(imorph
Morph
p145
(dp146
g75
(lp147
Vl
aVa
aVr
asba(imorph
Morph
p148
(dp149
g75
(lp150
Vl
aVa
aVr
aV\u0268
aVn
asbasbF635.41516280174255
tp151
asS'problem'
p152
S'Halle_85_Turkish'
p153
sS'finalFrontier'
p154
g6
(csolution
Frontier
p155
g8
NtRp156
(dp157
g71
g72
sg137
g138
sg86
g87
sS'frontiers'
p158
(lp159
(lp160
g13
aa(lp161
g52
aasbsS'parameters'
p162
g6
(cargparse
Namespace
p163
g8
NtRp164
(dp165
S'restore'
p166
NsS'features'
p167
S'simple'
p168
sS'universal'
p169
NsS'restrict'
p170
NsS'seed'
p171
S'0'
sS'serial'
p172
I00
sS'alignment'
p173
I00
sS'top'
p174
I1
sS'maximumDepth'
p175
I3
sS'window'
p176
NsS'minimizeBits'
p177
I5
sS'samples'
p178
I30
sS'save'
p179
NsS'resume'
p180
I00
sS'disableClean'
p181
I00
sS'stemBaseline'
p182
I30
sS'dummy'
p183
I00
sS'task'
p184
S'CEGIS'
p185
sS'geometry'
p186
NsS'verbosity'
p187
I0
sS'timeout'
p188
F24
sS'debug'
p189
NsS'cores'
p190
I40
sg152
S'Halle_85_Turkish'
p191
sS'mergeFrontiers'
p192
I00
sbsb.