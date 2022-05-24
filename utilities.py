# -*- coding: utf-8 -*-

import tempfile
import sys
import cPickle as pickle
import math
import random
import itertools
import traceback
import heapq

def sigmoid(x):
    return 1./(1. + math.exp(-x))

def average(l):
    return sum(l)/len(l)

def standardDeviation(l):
    u = average(l)
    return average([(x - u)**2 for x in l ])**0.5
def displayTimestamp(job):
    import datetime
    print job, '@', datetime.datetime.now()

def compose(f,g):
    return lambda x: f(g(x))
def mergeCounts(m,n):
    c = {}
    for f in set(m.keys() + n.keys()):
        c[f] = m.get(f,0.0) + n.get(f,0.0)
    return c
def scaleDictionary(s,d):
    return dict([ (k,v*s) for k,v in d.iteritems() ])
def isNumber(x):
    return isinstance(x, (int, long, float, complex))
def isFinite(x):
    return not (math.isnan(x) or math.isinf(x))
def lse(x,y):
    if not isFinite(x): return y
    if not isFinite(y): return x
    
    if x > y:
        return x + math.log(1 + math.exp(y - x))
    else:
        return y + math.log(1 + math.exp(x - y))
def lseList(l):
    a = l[0]
    for x in l[1:]: a = lse(a,x)
    return a
def normalizeLogDistribution(d, index = 0):
    z = lseList([t[index] for t in d ])
    return [t[:index] + (t[index]-z,) + t[index + 1:] for t in d ]
def safeLog(x):
    try: return math.log(x)
    except ValueError: return float('-inf')

def randomTestSplit(data,ratio):
    """ratio: what fraction is testing data. returns training,test"""
    testingSize = min(len(data) - 1, int(round(len(data)*ratio)))
    trainingSize = len(data) - testingSize
    shuffledData = list(data)
    random.shuffle(shuffledData)
    training, test = shuffledData[:trainingSize], shuffledData[trainingSize:]
    return [ x for x in data if x in training ], [ x for x in data if x in test ]

def flatten(xss):
    return [ x for xs in xss for x in xs ]

def randomlyRemoveOne(x):
    t = random.choice(x)
    return [ y for y in x if t != y ]
def randomlyPermute(l):
    l = list(l)
    random.shuffle(l)
    return l

def partitionEvenly(l,n):
    """partitions list l into n approximately equal portions"""
    minimumSize = int(len(l)/n)
    extras = len(l) - minimumSize*n

    partitions = []
    while len(l) > 0:
        size = minimumSize + int(extras > 0)
        partitions.append(l[:size])
        extras -= 1
        l = l[size:]
    assert len(partitions) == n
    return partitions
        

def everyBinaryVector(l,w):
    if l == 0:
        if w == 0: yield []
    elif w > -1:
        for v in everyBinaryVector(l - 1,w):
            yield [False] + v
        for v in everyBinaryVector(l - 1,w - 1):
            yield [True] + v

def randomPermutation(l):
    l = list(l)
    random.shuffle(l)
    return l

def everyPermutation(l,r):
    # every permutation of 0 -- (l-1)
    # each permutation is constrained to exchange exactly r elements
    assert r > 1
    for exchangedElements in itertools.combinations(range(l),r):
        for perm in itertools.permutations(exchangedElements):
            # every element has to be mapped to a new one
            if any([ p == e for p,e in zip(list(perm),list(exchangedElements)) ]): continue

            returnValue = list(range(l))
            for p,e in zip(list(perm),list(exchangedElements)):
                returnValue[e] = p
            yield returnValue

def dumpPickle(o,f):
    with open(f,'wb') as handle:
        pickle.dump(o,handle)
def loadPickle(f):
    with open(f,'rb') as handle:
        o = pickle.load(handle)
    return o

PARALLELMAPDATA = None
def lightweightParallelMap(numberOfCPUs, f, *xs, **keywordArguments):
    global PARALLELMAPDATA

    if numberOfCPUs == 1: return map(f,*xs)

    n = len(xs[0])
    for x in xs: assert len(x) == n
    
    assert PARALLELMAPDATA is None
    PARALLELMAPDATA = (f,xs)

    from multiprocessing import Pool

    # Randomize the order in case easier ones come earlier or later
    permutation = range(n)
    random.shuffle(permutation)
    inversePermutation = dict(zip(permutation, range(n)))

    # Batch size of jobs as they are sent to processes
    chunk = keywordArguments.get('chunk', 1)
    
    maxTasks = keywordArguments.get('maxTasks', None)
    workers = Pool(numberOfCPUs, maxtasksperchild = maxTasks)

    ys = workers.map(parallelMapCallBack, permutation,
                     chunksize = chunk)
    
    workers.terminate()

    PARALLELMAPDATA = None
    return [ ys[inversePermutation[j]] for j in range(n) ]


def parallelMapCallBack(j):
    global PARALLELMAPDATA
    f, xs = PARALLELMAPDATA
    try:
        return f(*[ x[j] for x in xs ])
    except Exception as e:
        print("Exception in worker during lightweight parallel map:\n%s"%(traceback.format_exc()))
        raise e


def parallelMap(numberOfCPUs, f, *xs):
    from pathos.multiprocessing import ProcessingPool as Pool
    
    if numberOfCPUs == 1: return map(f,*xs)
    def safeCall(x):
        try:
            y = f(*x)
            return y
        except Exception as e:
            print "Exception in worker during parallel map:\n%s"%(traceback.format_exc())
            raise e
    return Pool(numberOfCPUs).map(safeCall,zip(*xs))
            
            

def flushEverything():
    sys.stdout.flush()
    sys.stderr.flush()
def makeTemporaryFile(suffix, d = '.'):
    fd = tempfile.NamedTemporaryFile(mode = 'w',suffix = suffix,delete = False,dir = d)
    fd.write('')
    fd.close()
    return fd.name



VERBOSITYLEVEL = 0
def getVerbosity():
    global VERBOSITYLEVEL
    return VERBOSITYLEVEL
def setVerbosity(v):
    global VERBOSITYLEVEL
    VERBOSITYLEVEL = v

def sampleGeometric(p):
    if random.random() < p: return 0
    return 1 + sampleGeometric(p)


def numberOfCPUs():
    import multiprocessing
    return multiprocessing.cpu_count()

def indent(s):
    return '\t' + s.replace('\n','\n\t')

def multiLCS(xs):
    fragments = [ set([ tuple(x[starting:ending])
                        for starting in range(len(x))
                        for ending in range(starting + 1,len(x) + 1) ])
                  for x in xs ]
    fragmentsInCommon = fragments[0]
    for f in fragments[1:]: fragmentsInCommon = fragmentsInCommon&f
    return max(map(len,list(fragmentsInCommon)))

class PQ(object):
    """why the fuck does Python not wrap this in a class"""

    def __init__(self):
        self.h = []

    def push(self, priority, v):
        heapq.heappush(self.h, (-priority, v))

    def popMaximum(self):
        return heapq.heappop(self.h)[1]

    def __iter__(self):
        for _, v in self.h:
            yield v

    def __len__(self): return len(self.h)

def unique(xs):
    u = [xs[0]]
    for x in xs[1:]:
        if x in u: continue
        u.append(x)
    return u

def randomlyRemoveOne(xs):
    j = random.choice(range(len(xs)))
    return xs[:j] + xs[j + 1:]

def formatTable(t, separation = 5):
    columnSizes = [max([len(x[j]) for x in t ])
                   for j in range(len(t[0])) ]
    formatted = []
    for r in t:
        formatted.append(''.join([ x + ' '*(columnSizes[c] - len(x) + separation)
                                   for c,x in enumerate(r) ]).strip())
    return "\n".join(formatted)

class RunWithTimeout(Exception):
    pass

def runWithTimeout(k, timeout):
    import signal
    
    if timeout is None: return k()
    def timeoutCallBack(_1,_2):
        raise RunWithTimeout()
    signal.signal(signal.SIGPROF, timeoutCallBack)
    signal.setitimer(signal.ITIMER_PROF, timeout)
    
    try:
        result = k()
        signal.signal(signal.SIGPROF, lambda *_:None)
        signal.setitimer(signal.ITIMER_PROF, 0)
        return result
    except RunWithTimeout: raise RunWithTimeout()
    except:
        signal.signal(signal.SIGPROF, lambda *_:None)
        signal.setitimer(signal.ITIMER_PROF, 0)
        raise
            
        
        
def isPowerOf(n,p):
    q = 1
    while q < n:
        q = q*p
        if q == n: return True
    return False
