import os
import subprocess

import sys

DUMMY = len(sys.argv) > 1 and sys.argv[1] == "DUMMY"
def system(command):
    global DUMMY
    if DUMMY:
        print "Would now execute:"
        print command
    else:
        print "Will now execute:"
        print command
        os.system(command)

training = [
    "Odden_105_Bukusu",
    "Odden_81_Koasati",
    "Halle_125_Indonesian",
    "Odden_85_Samoan",
    "Odden_2.4_Tibetan",
    "Odden_1.3_Korean",
    "Odden_1.12_English",
    "Odden_2.1_Hungarian",
    "Odden_2.2_Kikuria",
    "Odden_2.5_Makonde",
    "Odden_3.1_Kerewe",
    "Odden_116_Armenian",
    "Odden_4.1_Serbo_Croatian",
    "Odden_4.4_Latin",
    "Odden_3.5_Catalan",
    "Odden_4.3_Somali",
    "Odden_3.3_Ancient_Greek",
    "Odden_68_69_Russian",
    "Odden_76_77_Kerewe",
    "Odden_77_78_English",
    "Odden_79_Jita",
    "Odden_81_Korean",
    "Roca_25_Zoque",
    "Roca_16_German",
    "Roca_89_Lumasaaba",
    "Roca_104_Tunica",
    "Halle_85_Turkish",
    "Halle_109_Russian",
    "Halle_149_Russian",
    "Odden_114_Lithuanian"
]

### Produce UG1
command = "pypy UG.py --export experimentOutputs/ug0.p"
for t in training:
    command += " experimentOutputs/%s_incremental_disableClean=False_features=sophisticated_geometry=True.p"%t

system(command)

print "expanding frontiers with new universal grammar!"
promises = []
for t in training:
    oldPath = "experimentOutputs/%s_incremental_disableClean=False_features=sophisticated_geometry=True.p"%t
    newPath = "experimentOutputs/%s_incremental_disableClean=False_features=sophisticated_geometry=True_expanded.p"%t
    command = "python driver.py %s frontier --geometry -t 100 --mergeFrontiers --restore %s --save %s -u experimentOutputs/ug0.p"%(t,
                                                                                                                                   oldPath,
                                                                                                                                   newPath)
    print "Will execute:",command
    promises.append(command)

if not DUMMY:
    promises = [subprocess.Popen(p, shell=True)
                for p in promises]
    for p in promises: p.wait()
print "Reestimate universal grammar!"
command = "pypy UG.py --export experimentOutputs/ug1.p"
for t in training:
    command += " experimentOutputs/%s_incremental_disableClean=False_features=sophisticated_geometry=True_expanded.p"%t

system(command)
