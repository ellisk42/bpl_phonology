from utilities import *
import os


os.system("python command_server.py %d&"%(numberOfCPUs()))
os.system("sleep 1")

canIgnore = set()
jobs = {}
for fn in os.listdir("experimentOutputs"):
    if "incremental"  not in fn:
        continue
    if "sophisticated" not in fn:
        continue
    if "geometry" not in fn:
        continue

    problem = fn[:fn.index("incremental")][:-1]
    if fn.endswith("_ug.p"): canIgnore = canIgnore|{problem}
    jobs[problem] = jobs.get(problem,set())|{fn}


for k in canIgnore:
    del jobs[k]

for problem, names in jobs.iteritems():
    print(problem)
    for n in names:
        print(n)
    assert len(names) == 1
    print

print "ignoring:",canIgnore

print len(jobs),len(canIgnore)

def issue(k):
    print "Issuing command:"
    print k
    os.system(k + " &")


for problem, names in jobs.iteritems():
    [name] = list(names)
    export = name.replace(".p","_finalExpansion.p")
    issue("python driver.py %s frontier --mergeFrontiers --features sophisticated --geometry -t 100  -u experimentOutputs/ug1.p --restore experimentOutputs/%s --save experimentOutputs/%s"%(problem,name,export))
    
print "and now we handle the alternation problems"

for fn in os.listdir("experimentOutputs/alternation"):
    if "simple" in fn: continue
    if "ablation" in fn: continue
    
    problem = fn.replace(".p","")
    issue("python alternation.py %s -t 100 --universal experimentOutputs/ug1.p"%problem)

while True:
    os.system("sleep 1")
