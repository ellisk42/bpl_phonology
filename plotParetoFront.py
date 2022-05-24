# -*- coding: utf-8 -*-

from utilities import *

from features import FeatureBank, tokenize, featureMap
from rule import Rule
from morph import Morph
from sketch import *
from matrix import UnderlyingProblem

from random import choice,seed
import matplotlib.pyplot as plot
import matplotlib.cm as cm
#from adjustText import adjust_text
import numpy as np
import argparse
import pickle


def removePointsNotOnFront(points):
    return sorted([ (x,y) for x,y in points
                    if not any([ a >= x and b >= y and (a,b) != (x,y)
                                 for a,b in points ])])

def plotParetoFront(solutions, solutionCosts):
    """solutionCosts: [(model cost,underlying form cost)]"""
    colors = cm.rainbow(np.linspace(0, 1, 1))
    plot.figure(figsize = (5,4))#(8,5))

    for i,xs in enumerate(sorted(solutions[0].underlyingForms.keys())):
        print "Example",i,xs

    ps = [(-p[0],-p[1]/float(len(solutions[0].underlyingForms)))
          for p in solutionCosts]
    plot.scatter([ p[0] for p in ps],
                 [ p[1] for p in ps],
                 alpha = 1.0/(1+2), s = 100, color = colors, label = 'Grammars')
            

    front = removePointsNotOnFront(ps)
    plot.plot([ x for x,y in front ], [ y for x,y in front ],'--', label = 'Pareto front')
    plot.ylabel("Fit to data (-average stem size)",fontsize = 12)
    plot.xlabel("Parsimony (-grammar size)",fontsize = 12)

    costToSolution = {(x,y): s
                      for (x,y),s in zip(ps,solutions) }
    W = max(p[0] for p in ps ) - min(p[0] for p in ps )
    ux = sum(p[0] for p in ps)/float(len(ps))
    H = max(p[1] for p in ps ) - min(p[1] for p in ps )
    uy = sum(p[1] for p in ps)/float(len(ps))
    minimumX = min(x for x,_ in costToSolution.keys() )
    maximumX = max(x for x,_ in costToSolution.keys() )
    dy = H/20.
    dx = W/5.
    text = []
    ax = plot.gca()
    if arguments.correct is not None:
        correct = list(sorted(costToSolution.iteritems()))[arguments.correct][1]
    else:
        correct = None

    if arguments.csv:
        for ii, ((x,y),_) in enumerate(list(sorted(costToSolution.iteritems()))):
            print "%s,%s,%s"%(-x,-y,ii==arguments.correct)

    if arguments.label:
        labels = {int(labelParameters[0]): (float(labelParameters[1]),float(labelParameters[2]),labelParameters[3],labelParameters[4])
                  for l in arguments.label
                  for labelParameters in [l.split("_")]}
    else:
        labels = []
        
    for si,((x1,y1),solution) in enumerate(sorted(costToSolution.iteritems())):
        print "Solution #",si
        print solution
        x2 = x1 - (2*int(x1 > ux) - 1)*dx
        y2 = y1 - (2*int(y1 > uy) - 1)*dy
        color = "wheat" if correct is None else "white"
        if correct is not None:
            if solution is correct: color = "pink"
            # elif False and any( r == rp
            #           for rp in correct.rules
            #           for r in solution.rules ) or \
            #               all( correct.prefixes[i] == solution.prefixes[i] and correct.suffixes[i] == solution.suffixes[i]
            #                   for i in range(len(correct.prefixes)) ):
            #     color = "pink"
        labelProperties = dict(boxstyle='round', facecolor=color, alpha=0.7)
        onFront = all( (xp == x1 and yp == y1) or yp < y1 or xp < x1
                       for xp,yp in costToSolution.keys() )
        if si in labels:
            x2,y2,orientation1,orientation2 = labels[si]
            text.append(plot.text(x2,y2, solution.pretty(),
                              fontsize=10,
                              bbox=labelProperties,
                                  verticalalignment = orientation1,
                              horizontalalignment = orientation2,
                              color = "k"))

            ax.annotate('',
                        xy = (x2,y2),xycoords = 'data',
                        xytext = (x1,y1),textcoords = 'data',
                        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3'))


    if arguments.title is not None:
        plot.title(arguments.title)

    if arguments.arrow:
        bbox_props = dict(boxstyle="rarrow,pad=0.3", fc="cyan", ec="b", lw=2)
        t = ax.text(max([x for x,y in solutionCosts ]), max([y for x,y in solutionCosts ]), "Better models", ha="center", va="center", rotation=45,
                    size=12,
                    bbox=bbox_props)

    if arguments.examples:
        examples = list(sorted(solutions[0].underlyingForms.keys()))
        examples = [u" ~ ".join(u"".join(ps.phonemes) for ps in examples[i])
                    for i in arguments.examples ]
        examples = u"\n".join(["Examples:"] + examples + (["..."] if len(examples) < len(solutions[0].underlyingForms) else []))
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        # place a text box in upper left in axes coords
        plot.text(0.05, 0.05, examples, transform=ax.transAxes,
                  fontsize=11, verticalalignment='bottom', horizontalalignment='left', bbox=props)

        print examples
        

    plot.legend(loc = 'lower center',fontsize = 9)
    if arguments.export:
        plot.tight_layout()
        plot.savefig(arguments.export)
        os.system("feh %s"%arguments.export)
    else:
        plot.show()




    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument("checkpoint")
    parser.add_argument("-t","--title",type=str,default=None)
    parser.add_argument("-e","--export",type=str,default=None)
    parser.add_argument("-l","--label",type=str,default=[],nargs='+')
    parser.add_argument("--examples",type=int,default=[],nargs='+')
    parser.add_argument("-c","--correct",type=int,default=None)
    parser.add_argument("-a","--arrow",action='store_true',default=False)
    parser.add_argument("--csv",action='store_true',default=False)
    
    arguments = parser.parse_args()
    
    with open(arguments.checkpoint,'rb') as handle:
        pf = pickle.load(handle)
        print(pf)
        
        if isinstance(pf,dict):
            pf = (list(pf.values()), list(pf.keys()))
    plotParetoFront(pf[0],pf[1])
