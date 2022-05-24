import re
from problems import *
from textbook_problems import *
from morph import Morph

from utilities import *
import pickle
import os
import sys

import numpy as np

from matplotlib.lines import Line2D
import matplotlib.pyplot as plot
plt = plot

ALTERNATIVEMETHODNAME = "SyPhon (2019)"

# these were not pickled correctly
alternation_timings_full_model = dict(zip(["Odden_A7_Kishambaa","Odden_A9_Palauan","Halle_51_Ganda","Odden_A3_Farsi","Odden_A1_Kikurai","Odden_A10_Quechua_Cuzco_dialect","Halle_55_Proto_Bantu","Odden_A4_Osage","Halle_53_Papago","Halle_59_Mohawk","Odden_A6_Gen","Odden_A8_Thai","Odden_A5_Amharic","Odden_A2_Modern_Greek","Odden_A11_Lhasa_Tibetan","Halle_49_Ewe"],
				   [13.072480916976929, 18.006218910217285, 72.40791988372803, 38.01783108711243, 189.97163200378418, 284.03229093551636, 35.32263207435608, 20.521980047225952, 67.20231604576111, 35.724035024642944, 71.97124910354614, 58.773473024368286, 103.82459211349487, 34.38520407676697, 324.7128210067749, 112.0015161037445]))
alternation_timing_simple = {}
alternation_timing_representation = {}
alternation_timing_representation['Halle_55_Proto_Bantu'] = 14.101643
alternation_timing_representation['Odden_A6_Gen'] = 18.872381
alternation_timing_representation['Halle_59_Mohawk'] = 18.949731
alternation_timing_representation['Odden_A7_Kishambaa'] = 28.401197
alternation_timing_representation['Odden_A9_Palauan'] = 27.280243
alternation_timing_representation['Odden_A8_Thai'] = 24.005453
alternation_timing_representation['Halle_49_Ewe'] = 25.311086
alternation_timing_representation['Odden_A3_Farsi'] = 42.159504
alternation_timing_representation['Odden_A5_Amharic'] = 22.015937
alternation_timing_representation['Halle_51_Ganda'] = 97.710196
alternation_timing_representation['Odden_A1_Kikurai'] = 50.656403
alternation_timing_representation['Halle_53_Papago'] = 21.745254
alternation_timing_representation['Odden_A4_Osage'] = 37.003790
alternation_timing_representation['Odden_A2_Modern_Greek'] = 10.615374
alternation_timing_representation['Odden_A10_Quechua_Cuzco_dialect'] = 132.635068
alternation_timing_representation['Odden_A11_Lhasa_Tibetan'] = 167.769529
alternation_timing_simple['Odden_A7_Kishambaa'] = 32.559811
alternation_timing_simple['Odden_A9_Palauan'] = 48.203088
alternation_timing_simple['Halle_59_Mohawk'] = 133.176063
alternation_timing_simple['Halle_51_Ganda'] = 183.522483
alternation_timing_simple['Odden_A6_Gen'] = 267.500649
alternation_timing_simple['Odden_A5_Amharic'] = 185.753106
alternation_timing_simple['Halle_49_Ewe'] = 337.858113
alternation_timing_simple['Halle_53_Papago'] = 127.711276
alternation_timing_simple['Odden_A3_Farsi'] = 236.915386
alternation_timing_simple['Odden_A4_Osage'] = 106.332940
alternation_timing_simple['Odden_A2_Modern_Greek'] = 56.475962
alternation_timing_simple['Odden_A8_Thai'] = 141.424669
alternation_timing_simple['Halle_55_Proto_Bantu'] = 57.470349
alternation_timing_simple['Odden_A11_Lhasa_Tibetan'] = 494.649122
alternation_timing_simple['Odden_A1_Kikurai'] = 330.273138
alternation_timing_simple['Odden_A10_Quechua_Cuzco_dialect'] = 400.175140
alternation_timing_baseline_dictionary = [alternation_timings_full_model,
                                          alternation_timing_simple,
                                          alternation_timing_representation]

def groundAccuracy(solution, problem, minimum=0.02):
    from grading import GoldSolution
    def normalize(stuff):
        return tuple(Morph(s) if s is not None else None
                     for s in stuff )

    problem = problem.key
    assert isinstance(problem,str)
    theTruth = {normalize(ss): \
                (set(Morph(possibility) for possibility in s) if isinstance(s,set) else Morph(s)) 
                for ss,s in GoldSolution.solutions[problem].underlyingForms.iteritems()}
    ff = solution
    if hasattr(ff,'finalFrontier'): ff = ff.finalFrontier
    thePrediction = {normalize(ss): Morph(s)
                     for ss,s in ff.underlyingForms.iteritems()}
    if not (set(thePrediction.keys()) <= set(theTruth.keys())):
        print "WARNING: you need to rerun",problem
        print "check out the following:"
        for difference in set(thePrediction.keys()) ^ set(theTruth.keys()):
            print difference
        
    
    numberCorrect = sum(thePrediction[theObservation] == gt or \
                        (isinstance(gt,set) and (thePrediction[theObservation] in gt))
                        for theObservation in thePrediction.keys()
                        for gt in [theTruth.get(theObservation,None)] )
    return max(numberCorrect/float(len(theTruth)), minimum)


class Bars():
    def __init__(self, problem, universal, fragment, *baselines):
        self.fragment = fragment
        self.problem = problem
        self.baselines = baselines
        self.universal = universal
        self.name = "%s (%s)"%(self.language, self.problem.source)
        print self.name, "Missing baseline?", any( b is None for b in baselines), "Missing full model?", self.universal is None

        self.Alternativemethod = None # do not have a Alternativemethod solution
        self.Alternativemethod_cc0 = None # the column cost zero Alternativemethod solution
        self.alternativemethod_time = None
        self.alternativemethod_column_time = None

        def get_alternativemethod_time(fn):
            with open(fn,"r") as handle:
                for ln in handle:
                    if "elapsed" in ln:
                        m = re.match(".*system ([0-9]+)\:([0-9]+)\.([0-9]+)elapsed .*",ln)
                        if m is not None:
                            return float(m.group(1))*60 + float(m.group(2))
                        m = re.match(".*system ([0-9]+)\:([0-9]+)\:([0-9]+)elapsed .*",ln)
                        if m is not None:
                            return float(m.group(1))*60*60 + float(m.group(2))*60 + float(m.group(3))
                        assert False
            return 24*60*60
        
        if self.alternation:
            if os.path.exists("CSV/"+self.problem.key+".output"):
                with open("CSV/"+self.problem.key+".output","r") as handle:
                    for ln in handle:
                        if "Successfully discovered rule" in ln:
                            self.Alternativemethod = 1.
                            break
                        if "Could not discover rule" in ln:
                            self.Alternativemethod = 0.
                            break
                assert self.Alternativemethod is not None
                # extract the amount of time that the baseline took
                self.alternativemethod_time = get_alternativemethod_time("CSV/"+self.problem.key+".output")
        else:
            fn1 = "CSV/"+self.problem.key+".output"
            fn2 = "CSV/"+self.problem.key+"_cc0.output"
            if os.path.exists(fn1):
                with open(fn1,"r") as handle:
                    content = handle.read()
                    if "Successful" in content: self.Alternativemethod = 1.
                    else: self.Alternativemethod = 0.
                    assert "could not be made bigger" not in content
                self.alternativemethod_time = get_alternativemethod_time(fn1)
            if os.path.exists(fn2):
                with open(fn2,"r") as handle:
                    content = handle.read()
                    if "Successful" in content: self.Alternativemethod_cc0 = 1.
                    else: self.Alternativemethod_cc0 = 0.
                    assert "could not be made bigger" not in content
                self.alternativemethod_column_time = get_alternativemethod_time(fn2)

    @property
    def alternation(self):
        return self.problem.parameters and "alternations" in self.problem.parameters

    @property
    def numberOfBars(self):
        return int(len(self.universal) > 0) + sum(b is not None for b in self.baselines)

    @property
    def language(self):
        if "Ukrainian" in self.problem.languageName: return "Ukrainian"
        return self.problem.languageName.replace(u" (Cuzco dialect)","")#self.problem.languageName

    def universalTime(self):
        if not self.alternation and self.universal:
            print self.name, "solved in", min(r.solutionSequence[-1][1] for r in self.universal), "seconds"

    def universalHeight(self, minimum=0):
        if self.alternation: return 1. # manually verified that all alternations are solved with universal
        if len(self.universal) == 0: return 0.
        assert len(self.universal) == 1
        if arguments.ground: return groundAccuracy(self.universal[0],self.problem,minimum)
        n = len(self.problem.data)
        return float(max(len(u.finalFrontier.underlyingForms) for u in self.universal))/n

    def averageBaselineHeight(self):
        return (self.AlternativemethodHeight() + sum(self.baselineHeight(b) for b in range(len(self.baselines)) ))/(len(self.baselines)+1)

    def AlternativemethodHeight(self,cc0=None,minimum=0.02):
        if cc0 is None: return max(self.AlternativemethodHeight(True, minimum=minimum), self.AlternativemethodHeight(False, minimum=minimum))
        
        if cc0: Alternativemethod = self.Alternativemethod_cc0
        else: Alternativemethod = self.Alternativemethod
        if Alternativemethod is None: return 0.
        if Alternativemethod == 0.: return minimum
        if Alternativemethod == 1.: return 1.
        assert False

    def AlternativemethodTime(self):
        x = self.Alternativemethod_cc0 or 0.
        y = self.Alternativemethod or 0.
        if x == y: return min(self.alternativemethod_column_time,self.alternativemethod_time)
        if x > y: return self.alternativemethod_column_time
        else: return self.alternativemethod_time

    def baselineHeight(self, b, minimum=0.02):
        if self.alternation:
            if b >= len(self.baselines) or self.baselines is None: return 0.
            if self.baselines[b] == "FAILURE": return minimum
            else: return 1.
        b = self.baselines[b]
        if b is None: return 0.
        if arguments.ground: return groundAccuracy(b,self.problem,minimum)
        n = len(self.problem.data)
        return max(float(len(b.finalFrontier.underlyingForms))/n, minimum)

    def fragmentHeight(self, minimum=0.02):
        if self.alternation:
            return 0.
        b = self.fragment
        if b is None: return 0.
        if arguments.ground: return groundAccuracy(b,self.problem,minimum)
        n = len(self.problem.data)
        return max(float(len(b.finalFrontier.underlyingForms))/n,minimum)

    def __str__(self):
        return "Bars(%s,%f)"%(self.name, self.universalHeight())

    def __repr__(self):
        return str(self)
        
def process_rule_grading(fn, precision_axes, recall_axes):
    import csv
    import matplotlib.pyplot as plt
    PRECISION = []
    RECALL = []
    with open(fn,"r") as handle:
        first_line = True
        for l in csv.reader(handle):
            if first_line:
                assert l[0] == "Language"
                first_line = False
                continue
            if len(l[0]) == 0: break

            np_ = int(l[1])
            nc = int(l[2])
            ns = int(l[3])
            ur = float(l[4])

            precision = float(nc)/(nc + ns)
            recall = float(nc)/np_

            PRECISION.append((ur,precision,np_))
            RECALL.append((ur,recall,np_))

    
    # PRECISION.sort(key=lambda tu: tu[-1])
    # RECALL.sort(key=lambda tu: tu[-1])
    permutation=list(range(len(PRECISION)))
    random.shuffle(permutation)
    PRECISION=np.array(PRECISION)[permutation]
    RECALL= np.array(RECALL)[permutation]

    processes = np.array(PRECISION[:,-1], dtype=int)
    
    
    coefficient = np.stack([1 - np.linspace(0,1.,max(processes)),
                            np.linspace(0,1.,max(processes))]).T
    low_color = np.array([1.,0.,0.])
    high_color = np.array([0.,0.,1.])
    color_choices = np.matmul(coefficient, np.stack([low_color,high_color]))
    colors = color_choices[processes - 1]
    alpha = 1
    
    PRECISION = np.array(PRECISION)
    RECALL = np.array(RECALL)
    from correlation import pearsonr
    precision_correlation = pearsonr(PRECISION[:,0], PRECISION[:,1], pretty=True)
    recall_correlation = pearsonr(RECALL[:,0], RECALL[:,1], pretty=True)
    print(precision_correlation, recall_correlation)
    
    
    W = 0.1
    unoise = np.random.random((len(processes)))*W-W/2
    pnoise = np.random.random((len(processes)))*W-W/2
    rnoise = np.random.random((len(processes)))*W-W/2
    
    precision_axes.scatter(PRECISION[:,0]+unoise,
                           PRECISION[:,1]+pnoise,
                           color=colors,
                           alpha=alpha)
    precision_axes.set_xlabel("% lexicon solved")
    precision_axes.set_ylabel("rule precision")
    precision_axes.spines["right"].set_visible(False)
    precision_axes.spines["top"].set_visible(False)

    is_outlier = PRECISION[:,0]==0.
    u_outlier = (PRECISION[:,0]+unoise)[is_outlier]
    p_outlier = (PRECISION[:,1]+pnoise)[is_outlier]
    r_outlier = (RECALL[:,1]+rnoise)[is_outlier]

    precision_axes.text(u_outlier, p_outlier, " **")

    recall_axes.scatter(RECALL[:,0]+unoise,
                        RECALL[:,1]+rnoise,
                        color=colors,
                        alpha=alpha)
    recall_axes.set_xlabel("% lexicon solved")
    recall_axes.set_ylabel("rule recall")
    recall_axes.spines["right"].set_visible(False)
    recall_axes.spines["top"].set_visible(False)

    precision_axes.set_yticks([0.,0.5,1.])
    recall_axes.set_yticks([0.,0.5,1.])

    recall_axes.text(u_outlier, r_outlier, " **")

    recall_axes.text(-0.0, 0.9, recall_correlation, fontsize=9)
    precision_axes.text(-0.00, 0.9, precision_correlation, fontsize=9)

    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    recall_axes.legend(handles=[Line2D([0], [0], marker='o', color='w', label='1 rule',
                                     markerfacecolor=color_choices[0], markersize=10, alpha=alpha)] + \
                              [Line2D([0], [0], marker='o', color='w',
                                      label='%d rules'%n if n == max(processes) else str(n),
                                      markerfacecolor=color_choices[n - 1], markersize=10)
                               for n in range(2,max(processes)+1) ],
                     ncol=max(processes),
                     loc='lower center',
                     bbox_to_anchor=(0.5,-0.5),
                     columnspacing=0.0,
                     handletextpad=0.)
    return 
    fig.subplots_adjust(bottom=0.25)

    plt.show()

            
                
            
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "Graphs the the system on all of the languages")
    parser.add_argument("--final","-f",action='store_true',default=False)
    parser.add_argument("--ground","-g",action='store_true',default=False)
    parser.add_argument("--universal","-u",action='store_true',default=False)
    parser.add_argument("--together","-t",action='store_true',default=False,
                        help="single matplotlib with everything")
    parser.add_argument("--include_alternation", "-a", action='store_true',default=False)
    parser.add_argument("--log", action='store_true',default=False)
    parser.add_argument("--csv", action='store_true',default=False)        
    parser.add_argument("--columns","-c",type=int,default=3)
    arguments = parser.parse_args()

    baselinePaths = ["experimentOutputs/%s_CEGIS_disableClean=False_features=sophisticated_geometry=True.p",
                     "experimentOutputs/%s_CEGIS_disableClean=False_features=simple.p",
                     "experimentOutputs/%s_CEGIS_disableClean=True_features=none.p"                     ]
    alternationBaselines = ["experimentOutputs/alternation/%s.p", # CEGIS, whatever
                            "experimentOutputs/alternation/%s_simple.p",
                            "experimentOutputs/alternation/%s_ablation.p"]
    universalPath = ["experimentOutputs/%s_incremental_disableClean=False_features=sophisticated_geometry=True.p"]
    fragmentPath = "experimentOutputs/%s_incremental_disableClean=False_features=sophisticated_geometry=True_ug.p"
    bars = []

    csv=[]

    for name, problem in Problem.named.iteritems():
        if problem.supervised: continue
        
        if "Kevin" in name: continue

        baselines = []
        universals = []
        fragment = None
        if problem.parameters and "alternations" in problem.parameters:
            if os.path.exists("experimentOutputs/alternation/%s.p"%name):
                universals.append(loadPickle("experimentOutputs/alternation/%s.p"%name))
            else:
                universals.append(None)
                print "Missing alternation",name

            for pathTemplate in alternationBaselines:
                if os.path.exists(pathTemplate%name):
                    bl = loadPickle(pathTemplate%name)
                    if bl is None: bl = "FAILURE"
                else:
                    bl = None
                baselines.append(bl)
        else:
            for pathTemplate in baselinePaths:
                if os.path.exists(pathTemplate%name):
                    bl = loadPickle(pathTemplate%name)
                    print "Loaded", pathTemplate%name
                else:
                    bl = None
                    print "Missing baseline",pathTemplate%name
                baselines.append(bl)
            
            for u in universalPath:
                if os.path.exists(u%name):
                    universals.append(loadPickle(u%name))

            if os.path.exists(fragmentPath%name):
                fragment = loadPickle(fragmentPath%name)
                print "Loaded",fragmentPath%name
        
        bars.append(Bars(problem,universals,fragment,*baselines))

    # for b in bars:
    #     b.universalTime()
    # assert False

    bars.sort(key=lambda b: (-b.universalHeight(), b.fragment is not None,not b.alternation, -b.universalHeight(), -(b.averageBaselineHeight())))

    if arguments.final:
        for n,b in enumerate(bars):
            if b.alternation: b.name = b.problem.languageName + "*"
            else:
                if sum(b.language == o.language for o in bars if not b.alternation ) > 1:
                    i = sum(b.language == o.language for o in bars[:n + 1]
                            if not b.alternation)
                    b.name = b.language + " (" + "I"*i + ")"
                else:
                    b.name = b.language
            b.name = b.name.replace(" (Cuzco dialect)","")


    columns = arguments.columns
    if arguments.universal:
        csv.append(["", "language", "% lexicon solved w/ fragment grammar", "% lexicon solved w/o fragment grammar"])
        bars = [b for b in bars if b.fragment is not None]
        for b in bars:
            print(b.name,b.fragmentHeight(),b.universalHeight())
            csv.append(["", b.name,
                        str(b.fragmentHeight(minimum=0)),
                        str(b.universalHeight(minimum=0))])
            
            
        ys = np.arange(len(bars))
        W = (1 - 0.2)/2
        colors = [("before learning fragment grammar","#bc5090"),
                  ("with learned fragment grammar","#003f5c")]
        plot.bar(ys - W/2, [b.universalHeight() for b in bars],W,color=colors[0][1])
        plot.bar(ys + W/2, [b.fragmentHeight() for b in bars],W,color=colors[1][1])
        plot.gca().set(xticks=ys - W,
                       xticklabels=[b.name for b in bars ])
        plot.xticks(rotation=45)
        plot.ylabel("% lexicon solved")
        plot.gca().spines['right'].set_visible(False)
        plot.gca().spines['top'].set_visible(False)
        plot.gca().set_xlim(-W*1.5, len(bars)-W*0.5)

        geometryAverage = sum([b.universalHeight() for b in bars])/len(bars)
        fragmentAverage = sum([b.fragmentHeight() for b in bars])/len(bars)
        print(geometryAverage,fragmentAverage,fragmentAverage/geometryAverage)


        
        plot.legend([Line2D([0],[0],color=c,lw=4)
                     for _,c in colors],
                    [n for n,_ in colors ],
                    ncol=2,
                    loc='lower center',
                    bbox_to_anchor=(0.5,-1))
        plot.show()

        if arguments.csv:
            print u"\n".join([u",".join(l) for l in csv ])
        sys.exit()


    #f = plt.figure()

    if arguments.together:
        rows = 2
        f, axes = plt.subplots(rows, columns, gridspec_kw={'height_ratios': [3, 1]})
        bar_axes = axes[0]
    else:
        rows = 1
        f, axes = plt.subplots(rows, columns)
        bar_axes = axes

    
     
    # partition into columns
    partitions = partitionEvenly(bars,columns)
    #f.yticks(rotation=45)
    colors = [("ours (full)", "b"),
              ("ours (CEGIS)", "purple"),
              ("ours (simple features)", "mediumslateblue"),
              ("-representation", "teal"),
              (ALTERNATIVEMETHODNAME, "gold")]
    number_of_baselines = len(colors) - 1
    colormap = dict(colors)
    for pi,(a,bs) in enumerate(zip(bar_axes,partitions)):
        bs.reverse()
        
        W = (1 - 0.2)/(len(colors))
        ys = np.arange((len(bs)))
        
        a.barh(ys + W*number_of_baselines,
               [b.universalHeight() for b in bs ],
               W,
               color=colormap["ours (full)"])
        a.spines['right'].set_visible(False)
        a.spines['top'].set_visible(False)
        
        for bi,(name,c) in enumerate(colors[1:-1]):
            a.barh(ys + W*(len(colors) - 2 - bi),
                   [b.fragmentHeight() if name == "FG" else b.baselineHeight(bi)
                    for b in bs ],
                   W,
                   color=c)

        a.barh(ys,
               [b.AlternativemethodHeight() for b in bs ],
               W,
               color=colormap[ALTERNATIVEMETHODNAME])

        print "names",[b.name for b in bs ]

        a.set(yticks=ys + 2*W,
              yticklabels=[b.name for b in bs ])
        a.set_ylim(-W,len(bs))
        if pi == int(columns/2):
            a.set_xlabel('% lexicon solved' if arguments.ground else '% data covered')

        for b in bs:            
            csv.append([b.name]+map(str, [b.universalHeight(minimum=0.0),
                                          b.baselineHeight(0, minimum=0.0),
                                          b.baselineHeight(1, minimum=0.0),
                                          b.baselineHeight(2, minimum=0.0),
                                          b.AlternativemethodHeight(minimum=0.0)]))


    print "Heights:",[b.universalHeight() for b in bars ]
    

    bar_axes[len(bar_axes)//2].legend([Line2D([0],[0],color=c,lw=4)
                 for _,c in colors],
                                      [n for n,_ in colors ],
                                      ncol=len(colors),
                                      loc='lower center',
                                      bbox_to_anchor=(0.5,-0.2),
    )
    print len(bars),"data sets"
    print len({b.language for b in bars }),"distinct languages"

    
    if not arguments.together:
        plot.show()
        f, axes = plt.subplots(rows, columns)
        precision_axes = axes[1]
        recall_axes = axes[2]
        timing_axes = axes[0]
    else:
        precision_axes = axes[1,1]
        recall_axes = axes[1,2]
        timing_axes = axes[1,0]
        
    print({b.language for b in bars })

    process_rule_grading("grades.csv",precision_axes,recall_axes)

    candidates = [b for b in bars if arguments.include_alternation or not b.alternation]
    
    day = 24*60*60
    
    full_model_curve = []
    baseline_curves = [list() for _ in range(number_of_baselines) ]

    TIMES = np.linspace(60 if arguments.log else 0.,day,1000)
    
    for b in candidates: # for each language
	if b.alternation:
            full_model_curve.append([(alternation_timings_full_model[b.problem.key],
                                      1.)])
            for baseline_index in range(0, number_of_baselines - 1):
                baseline_curves[baseline_index].append([(alternation_timing_baseline_dictionary[baseline_index][b.problem.key],
                                                         b.baselineHeight(baseline_index, minimum=0.))])
        else:
            def my_accuracy(s):
	        return groundAccuracy(solution,b.problem,minimum=0)
            
	    curve = [ (time,my_accuracy(solution))
		  for solution, time in  b.universal[0].solutionSequence]
#	    curve.append((day - 1,curve[-1][-1]))
            full_model_curve.append(curve)


            for baseline_index in range(number_of_baselines - 1): # Alternativemethod baseline is different
                curve = [ (time,my_accuracy(solution))
                          for solution, time in  b.baselines[baseline_index].solutionSequence]
                #curve.append((day,curve[-1][-1]))
                baseline_curves[baseline_index].append(curve)

        # works both with and without alternations
        curve = [(b.AlternativemethodTime(), b.AlternativemethodHeight(minimum=0.))]
        baseline_curves[-1].append(curve)

        
	
    def curve_height(t,cs):
	ys = [max([0]+[y for _t,y in _cs if _t <= t ])
	      for _cs in cs ]
	mu = sum(ys)/len(ys)
	s = sum((y - mu)**2 for y in ys )/len(ys)
	
	return mu, s**0.5

    def curve_csv(cs, name):
        csv.append(["", name])
        csv.append(["", "", "time (seconds)", "% lexicon solved across problems --->"])
        previous_height=None
        for t in TIMES:
            if curve_height(t, cs)!=previous_height:
                ys = [max([0]+[y for _t,y in _cs if _t <= t ])
	              for _cs in cs ]
                csv.append(["", "", str(t)]+map(str, ys))

    
    universal_height = [curve_height(t,full_model_curve) for t in TIMES ]
    timing_axes.plot([t/float(day) for t in TIMES ],
		      [(y + 0) for y,s in universal_height ],
	      color=colors[0][1],label=colors[0][0])
    timing_axes.fill_between([t/float(day) for t in TIMES ],
		      [y + s/math.sqrt(len(candidates)) for y,s in universal_height ],
		      [y - s/math.sqrt(len(candidates)) for y,s in universal_height ],
		      color=colors[0][1], alpha=0.1)

    curve_csv(full_model_curve, "full model")
    
    
    print("full model accuracy/deviation", universal_height[-1])

    for baseline_index in range(number_of_baselines):
        baseline_height = [curve_height(t,baseline_curves[baseline_index]) for t in TIMES ]
        print("baseline", baseline_index, "accuracy/deviation", baseline_height[-1])
        timing_axes.plot([t/float(day) for t in TIMES ],
                  [(y + 0) for y,s in baseline_height ],
                  color=colors[baseline_index+1][1],label=colors[baseline_index+1][0])
        timing_axes.fill_between([t/float(day) for t in TIMES ],
                          [y + s/math.sqrt(len(candidates)) for y,s in baseline_height ],
                          [y - s/math.sqrt(len(candidates)) for y,s in baseline_height ],
                          color=colors[baseline_index+1][1], alpha=0.1)

        curve_csv(baseline_curves[baseline_index], colors[baseline_index+1][0])

    if arguments.log: timing_axes.set_xscale('log')
    
    timing_axes.set_xlabel('time (days)')
    timing_axes.set_ylabel('avg % lexicon solved')
    if not arguments.together: timing_axes.legend()

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.7, hspace=0.46,
                        left=0.13, right=0.5,
                        top=0.96, bottom=0.18)
    plot.show()

    timings = []
    for b in candidates:
        if b.alternation: continue
        
        timings.append((b.baselines[0].solutionSequence[-1][-1],
        		b.universal[0].solutionSequence[-1][-1]))
    
    
    statistics = [y for x,y in timings ]
    #statistics.extend(list(alternation_timings_full_model.values()))
    mean = sum(statistics)/len(statistics)
    deviation = (sum( (t - mean)**2 for t in statistics )/len(statistics))**0.5
    print "average runtime",mean/day,"standard deviation", deviation/day

    if arguments.csv:
        print "\n".join([",".join(l) for l in csv ])
