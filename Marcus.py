# -*- coding: utf-8 -*-

from utilities import *

from features import FeatureBank, tokenize, featureMap
from rule import Rule
from morph import Morph
from sketch import *
from matrix import UnderlyingProblem

from random import choice,seed
import numpy as np
import argparse

from command_server import start_server

seed(4)

TEMPERATURE = 2.0

stimuliFromLiterature = {
    "aax": [u"leledi",u"wiwidi",u"jijidi",u"dededi"],
    "aab": [u"leledi",u"wiwije",u"jijili",u"dedewe"],
    "aba": [u"ledile",u"wijewi",u"jiliji",u"dewede"],
    "Chinese": [u"manmandə",u"leledə",u"xawxawdə"]
    }

def sampleVowel():
    return choice([u"i",u"ɩ",u"e",u"ə",u"ɛ",u"æ",u"a",u"u",u"ʊ",u"o",u"ɔ"])
def sampleConsonant():
    return choice([u"p",u"b",u"f",u"v",u"m",u"θ",u"d",u"t",u"ð",u"z",u"ǰ",u"s",u"n",u"š",u"k",u"g",u"ŋ",u"h",u"w",u"r",u"l"])
def sampleSyllable():
    v = sampleVowel()
    k = sampleConsonant()
    return k + v
def sampleAB():
    while True:
        s = sampleSyllable()
        d = sampleSyllable()
        return s,d
def sampleABA(n):
    l = []
    for _ in range(n):
        s,d = sampleAB()
        l.append(s + d + s)
    return l
def sampleABB(n):
    l = []
    for _ in range(n):
        s,d = sampleAB()
        l.append(d + s + s)
    return l
def sampleAAB(n):
    l = []
    for _ in range(n):
        s,d = sampleAB()
        l.append(s + s + d)
    return l
def sampleABX(n,X=None):
    l = []
    x = X or sampleSyllable()
    for _ in range(n):
        s,d = sampleAB()
        l.append(s + d + x)
    return l
def sampleAXA(n,X=None):
    l = []
    x = X or sampleSyllable()
    for _ in range(n):
        a = sampleSyllable()
        l.append(a + x + a)
    return l
def sampleAAX(n,X=None):
    l = []
    x = X or sampleSyllable()
    for _ in range(n):
        a = sampleSyllable()
        l.append(a + a + x)
    return l

def removePointsNotOnFront(points):
    return sorted([ (x,y) for x,y in points
                    if not any([ a >= x and b >= y and (a,b) != (x,y)
                                 for a,b in points ])])


if __name__ == '__main__':
    start_server(1)
    parser = argparse.ArgumentParser(description = 'Generate and analyze synthetic rule learning problems ala Gary Marcus ABA/ABB patterns')
    parser.add_argument('-p','--problem', default = 'abb',
                        choices = ["aba","aab","abb","abx","aax", "axa","Chinese"],
                        type = str)
    parser.add_argument('-t','--top', default = 1, type = int)
    parser.add_argument('-d','--depth', default = 3, type = int)
    parser.add_argument('-n','--number', default = 4, type = int)
    parser.add_argument('-q','--quiet', action = 'store_true')
    parser.add_argument('--noSyllables', action = 'store_true')
    parser.add_argument('--save', default = None, type = str)
    parser.add_argument('--load', default = None, type = str)
    parser.add_argument('--animationStage', default = 99, type = int)
    parser.add_argument('--export', action = 'store_true')
    
    arguments = parser.parse_args()

    sampling = {'aba': sampleABA,
                'abb': sampleABB,
                'abx': sampleABX,
                'aax': sampleAAX,
                'axa': sampleAXA,
                'aab': sampleAAB,
                }
    constantPrefix = arguments.problem.startswith('x')
    constantSuffix = arguments.problem.endswith('x')

    if arguments.problem in stimuliFromLiterature:
        trainingData = stimuliFromLiterature[arguments.problem][:arguments.number]
        if len(trainingData) < arguments.number:
            if 'x' in arguments.problem:
                assert arguments.problem == 'aax'
                trainingData += sampling[arguments.problem](arguments.number - len(trainingData),
                                                            X='di')
            else:
                trainingData += sampling[arguments.problem](arguments.number - len(trainingData))
    else:
        trainingData = sampling[arguments.problem](arguments.number)
    
    print u"\n".join(trainingData)
    surfaceLength = sum([len(tokenize(w)) for w in trainingData ])

    costToSolution = {}
    if arguments.load != None:
        assert not arguments.quiet
        costToSolution = loadPickle(arguments.load)
    else:
        worker = UnderlyingProblem([(w,) for w in trainingData ],
                                   useSyllables = not arguments.noSyllables)
        solutions, costs = worker.paretoFront(arguments.depth, (arguments.top+1)//2, TEMPERATURE,
                                              useMorphology = True,
                                              morphologicalCoefficient = 4,
                                              offFront=arguments.top//2)
        for solution, cost in zip(solutions, costs): costToSolution[cost] = solution

    if arguments.save != None:
        assert arguments.load == None
        assert str(arguments.number) in arguments.save
        assert arguments.problem in arguments.save
        dumpPickle(costToSolution, arguments.save)

    import matplotlib.pyplot as plot
    import matplotlib.cm as cm        
        
    colors = cm.rainbow(np.linspace(0, 1, 1))
    if not arguments.quiet:
        plot.figure(figsize = (8,5))
        #plot.rc('text', usetex=True)
        #plot.rc('font', family='serif')
        if arguments.animationStage > 1:
            plot.scatter([ -p[0] for p in costToSolution],
                         [ -p[1]/float(arguments.number) for p in costToSolution],
                         alpha = 1.0/(1+2), s = 100, color = colors, label = 'Grammars')
        plot.ylabel("Fit to data (-average stem size)",fontsize = 14)
        plot.xlabel("Parsimony (-grammar size)",fontsize = 14)
        plot.title("Pareto front for %s, %d example%s%s"%(arguments.problem,
                                                          arguments.number,
                                                          '' if arguments.number == 1 else 's',
                                                          ', w/o syllables' if arguments.noSyllables else ''))
                
        # these are matplotlib.patch.Patch properties
        ax = plot.gca()
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        # place a text box in upper left in axes coords
        plot.text(0.05, 0.05, u"\n".join(["Examples:"] + trainingData), transform=ax.transAxes,
                  fontsize=14, verticalalignment='bottom', horizontalalignment='left', bbox=props)

        front = removePointsNotOnFront([ (-c1,-c2/float(arguments.number)) for c1,c2 in costToSolution.keys() ])
        # diagram the front itself
        if arguments.animationStage > 2:
            plot.plot([ x for x,y in front ], [ y for x,y in front ],'--', label = 'Pareto front')

        # Decide which points to label with the corresponding program
        solutionsToLabel = list(front)
        for c2 in { c2 for c1,c2 in costToSolution }:
            y = -c2/float(arguments.number)
            # candidates that are not on the front
            candidates = [ -c1 for c1,_c2 in costToSolution if _c2 == c2 and not (-c1,y) in front ]
            if candidates != [] and choice([False,True,False]):
                chosen = choice(candidates)
                solutionsToLabel.append((chosen,y))

        xs = []
        ys = []
        # illustrate the synthesized programs along the front
        dy = 0.5
        dx = 2
        text = []
        for c1,c2 in sorted(costToSolution.keys(), key = lambda cs: (cs[1],cs[0])):
            solution = costToSolution[(c1,c2)]
            x1 = -c1
            y1 = -c2/float(arguments.number)
            fronting = 1 if (x1,y1) in front else -1
            x2 = x1 + fronting*dx
            y2 = y1 + fronting*dy
            print x2,y2
            print solution.pretty()

            xs += [x1,x2]
            ys += [y1,y2]

            if not (x1,y1) in solutionsToLabel: continue

            assert not any( r.doesNothing() for r in solution.rules )
            
            #don't show anything which is two big because it will take up too much space on the graph
            if fronting == -1 or True:
                if any( len(r.pretty()) > 20 for r in solution.rules ): continue
                if len(solution.pretty().split(u"\n")) > 3: continue
                
            
            if arguments.animationStage > 3:
                color = "white"
                if u"σ" in solution.pretty():
                    color = "pink"
                if len(solution.rules) == 1 and u"σ" in solution.pretty():
                    if all( len(affix) == 2*constantPrefix for affix in solution.prefixes) and \
                       all( len(affix) == 2*constantSuffix for affix in solution.suffixes):
                        color = "red"
                labelProperties = dict(boxstyle='round', facecolor=color, alpha=0.7)

                # if color != 'red':
                #     if 'surface' not in solution.pretty() and random() < 0.5: continue

                text.append(plot.text(x2,y2, solution.pretty(),
                                      fontsize=10,
                                      bbox=labelProperties,
                                      verticalalignment = 'bottom' if fronting == 1 else 'top',
                                      horizontalalignment = 'center',
                                      color = "k"))
                
                ax.annotate('',
                            xy = (x2,y2),xycoords = 'data',
                            xytext = (x1,y1),textcoords = 'data',
                            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3'))
        
        # from adjustText import adjust_text
        # if arguments.animationStage > 3:
        #     adjust_text(text, autoalign = 'xy',
        #                 arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3'))


        if arguments.animationStage > 0:
            bbox_props = dict(boxstyle="rarrow,pad=0.3", fc="cyan", ec="b", lw=2)
            t = ax.text(max([x for x,y in solutionsToLabel ]), max([y for x,y in solutionsToLabel ]), "Better models", ha="center", va="center", rotation=45,
                        size=12,
                        bbox=bbox_props)


        plot.xlim([min(xs) - 1,max(xs) + 1])
        plot.ylim([min(ys) - 1,max(ys) + 1])
        plot.legend(loc = 'lower center',fontsize = 9)
        if arguments.export:
            export = '../../phonologyPaper/%s%d.png'%(arguments.problem,arguments.number)
            plot.savefig(export)#,bbox_inches = 'tight')
            os.system('feh %s'%export)
        else:
            plot.show()
