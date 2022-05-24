# -*- coding: utf-8 -*-

from grading import GoldSolution
from solution import *
from features import featureMap,tokenize
from parseSPE import *

from result import *
#from solution import *
from morph import *
from problems import *
from textbook_problems import *

import cPickle as pickle
import os

universal_training = [
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
        "Odden_114_Lithuanian",
    ]


latexMap = {
    u"f^y": "f\\super j",
    u"ɲ̩": "\\s{\\textltailn}",
    u"ŋ̩": "\\s{N}",
    u"l̥": u"\\r*l",
    u"m̩": u"\\s{m}",
    u"n̩": u"\\s{n}",
    u"x̯": u"\\textsubarch{x}",
    u"p^y": "p\\super j",
    u"ł": "\\textbeltl ",
    u"n̆": "\\u{n}",
    u"ɲ": "\\textltailn ",
    u"ɉ": "J",
    u"ç": "\\c{c}",
    u"ɨ": '1',
    u"ɯ": 'W',
    u"ɩ": '\\textiota ',
    u"ə": '@',
    u"ɛ": 'E',
    u"ʌ": '2',
    u"æ": '\\ae ',
    # rounded vowels
    u"ü": '\\"u',
    u"ʊ": 'U',
    u"ö": '\\"o',
    u"ɔ": 'O',
    #possibly missing are umlauts

    # consonance
    u"ṛ": "\\.*r",
    u"n^y": "n\\super j",
    u"r^y": "r\\super j",
    u"s^y": "s\\super j",
    u"z^y": "z\\super j",
    u"b^y": "b\\super j",
    u"t^s^y": "r\\super s \\super j",
    u"d^y": "d\\super j",
    u"ħ": "\\textcrh ",
    u"ʕ": 'Q',
    u"m^y": "m\\super j",
    u"t^y": "t\\super j",
    u"ṇ": '\\.*n',
    u"l^y": "l\\super j",
    u"v^y": "v\\super j",
    u"š^y": "S\\super j",
    u"y": 'j',
    u"p̚": 'p\\textcorner ',
    u"p^h": 'p\\super h',
    u"g^h": 'g\\super h',
    u"b^h": 'b\\super h',
    u"β": 'B',
    u"β|": 'B',
    u"φ": 'F',
    u"φ|": 'F',
    u"m̥": '\\r*m',
    u"θ": 'T',
    u"d^z": 'd\\super z',
    u"d^z^h": 'd\\super z\\super h',
    u"t̚": 't\\textcorner ',
    u"t^s": 't\\super s',
    u"t^h": 't\\super h',
    u"ṭ": '\\.*t',
    u"ḍ": '\\.*d',
    u"ð": 'D',
    u"ǰ": 'd\\super Z',#'\\v{j}',
    u"ž": 'Z',#'\\v{z}',
    u"ž^y": 'Z\\super j',#'\\v{z}',
    u"n̥": '\\r*n',
    u"ñ": '\\~n',
    u"š": 'S',#'\\v{s}',
    u"č": 't\\super S',#'\\v{c}',
    u"č^y": 't\\super S\\super j',#'\\v{c}',
    u"č^h": 't\\super S\\super h',#'\\v{c}\\super h',
    u"k̚": 'k\\textcorner ',
    u"k^h": 'k\\super h',
    u"k^y": 'k\\super j',
    u"x": 'x',
    u"χ": 'x',
    u"x^y": 'x\\super j',
    u"g^y": 'g\\super j',
    u"ɣ": 'G',
    u"ɣ^y": 'G\\super j',
    u"ŋ": 'N',
    u"N": '\\;N',
    u"G": '\\;G',
    u"ʔ": 'P',
    u"r̃": '\\~r',
    u"r̥̃": '\\r*{\\~r}',
    u"ř": '\\v{r}',
    u"ṣ": '\\:s',
    u"w̥": '\\r*{w}'
}

# tone stuff
for v in featureMap:
    if "vowel" in featureMap[v]:
        latexMap[v + u"́"] = '\\\'{' + latexMap.get(v,v) + '}'
        latexMap[v + u"`"] = '\\\'={' + latexMap.get(v,v) + '}'
        latexMap[v + u"¯"] = '\\={' + latexMap.get(v,v) + '}'
        latexMap[v + u":"] = latexMap.get(v,v) + ':'
        latexMap[v + u"́:"] = '\\\'{' + latexMap.get(v,v) + '}' + u':'
        latexMap[v + u"̌"] = '\\|x{' + latexMap.get(v,v) + '}'
        latexMap[v + u"̃"] = '\\~' + latexMap.get(v,v)
        latexMap[u"̌" + v] =  '\\|x{' + latexMap.get(v,v) + '}'


def latexWord(w):
    if w == None: return " -- "
    if not isinstance(w,Morph): w = Morph(w)
    return "\\textipa{" + "".join([ latexMap.get(p,p) for p in w.phonemes ]) + "}"
            

def latexMatrix(m):
    r = "\\begin{tabular}{%s}\n"%("c"*len(m[0]))
    r += "\\\\\n".join([ " & ".join([latexWord(w) for w in l ])
                         for l in m ])
    r += "\n\\end{tabular}\n"
    return r

def latexAlternation(solution, problem):
    languageName = problem.languageName

    r = "\\emph{%s:}\\\\"%(problem.languageName.replace('-','--'))
    
    r += "\\begin{longtable}{%s}\\toprule\n"%("ll")
    r += " & ".join([ "Surface form","UR"])
    r += "\n\\\\ \\midrule\n"
    for x in problem.data:
        r += latexWord(x) + "&"
        r += latexWord(solution.applySubstitution(Morph(x)))
        r += "\\\\\n"
    r += "\\bottomrule\\end{longtable}\n\n"
    r += "\\begin{longtable}{ll}\\toprule\n"
    r += "\\emph{The surface form...}&\\emph{Is underlyingly...}"
    r += "\n\\\\ \\midrule\n"
    for k,v in solution.substitution.iteritems():
        r += latexWord(k) + "&" + latexWord(v)
        r += "\\\\\n"
    r += "\\bottomrule\\end{longtable}\n\n"

    rules = solution.rules
        
        

    r += '''\n\\begin{tabular}{l}\\emph{Rules: }\\\\
%s
\\end{tabular}'''%("\\\\".join([ r.latex() for r in rules if not r.doesNothing() ]))
    
    return r

def latexMatrixProblem(result,idx=None):
    assert isinstance(result,Result)
    problem = Problem.named[result.problem]
    language = problem.languageName

#    r = "\\emph{%s} \\verb|%s| \\emph{%s%s:}\\\\"%(language.replace('-','--'),problem.key,
    r = "\\emph{%s} \\emph{%s%s:}\\\\"%(language.replace('-','--'),
                               "" if idx is None else (" (problem %d)"%idx),
                               "" if result.problem not in universal_training else (" (in metatheory training set)"))

    solution = result.finalFrontier.MAP(universal)

    if result.problem == "Odden_2.4_Tibetan":
        # this is wonky
        # paradigm format: (in-isolation, ten+num, num+ten)
        ten = solution.underlyingForms[(Morph(u"ǰu"),None,None)]
        solution.prefixes = [Morph([]),ten,Morph([])]
        solution.suffixes = [Morph([]),Morph([]),ten]
        
    correctAnswer = {tuple(None if zz is None else Morph(zz)
                               for zz in ss): \
                     (set(Morph(possibility) for possibility in s) if isinstance(s,set) else Morph(s))
                         for ss,s in GoldSolution.solutions[problem.key].underlyingForms.iteritems()}

    if result.problem == "Odden_3.7_Korean":
        # transpose
        r += "\\\\(note: the data is shown transposed because otherwise it does not fit on the PDF page)\\\\"
        r += "\\begin{longtable}{l|%s}\\toprule\n"%("l"*len(GoldSolution.solutions[problem.key].underlyingForms) + "")
        numberOfInflections = len(GoldSolution.solutions[problem.key].prefixes)
        for i in range(numberOfInflections):
            prefix = solution.prefixes[i]
            suffix = solution.suffixes[i]
            if len(prefix) > 0: r += latexWord(prefix) + "$+$\\\\"
            r += "stem$+$"
            if len(suffix) > 0: r += "\\\\" + latexWord(suffix)
            r += " & "
            r += " & ".join(latexWord(surfaces[i])
                            for surfaces in problem.data)
            r += "\\\\\\\\\n"
        r += "\\midrule\\^{UR}& "
        r += " & ".join(latexWord(solution.underlyingForms[ss]) if ss in solution.underlyingForms else "--"
                        for surfaces in problem.data
                        for ss in [tuple(None if s is None else Morph(s)
                                         for s in surfaces )] )
        r += "\\\\\n"
        r += "UR&"
        r += " & ".join(latexWord(GoldSolution.solutions[problem.key].underlyingForms[surfaces])
                        for surfaces in problem.data
                        for ss in [tuple(None if s is None else Morph(s)
                                         for s in surfaces )] )
        r += "\n\\\\"        
    else:# normal            
        r += "\\begin{longtable}{%s}\\toprule\n"%("l"*len(GoldSolution.solutions[problem.key].prefixes) + "|ll")
        if result.problem in ["Odden_3.1_Kerewe","Odden_79_Jita"]:
            # this one is too big but we can make it fit if we stack the morphology
            r += " & ".join([ "\\begin{tabular}{c}" + \
                              ("" if len(p) == 0 else latexWord(p) + "$+$") + \
                              "\\\\stem\\\\" + \
                              ("" if len(s) == 0 else "$+$" + latexWord(s)) + "\\end{tabular}"
                              for p,s in zip(solution.prefixes, solution.suffixes) ] + ["\\^{UR}","UR"])
        else:
            r += " & ".join([ ("" if len(p) == 0 else latexWord(p) + "$+$") + "stem" + ("" if len(s) == 0 else "$+$" + latexWord(s))
                          for p,s in zip(solution.prefixes, solution.suffixes) ] + ["\\^{UR}","UR"])
        r += "\n\\\\ \\midrule\n"
        for observation in problem.data:
            observation = tuple([Morph(oo) if oo is not None else None for oo in observation ])
            ur = solution.underlyingForms.get(observation,None)
            gt = correctAnswer[observation]
            if isinstance(gt,set):
                gt = "/".join(latexWord(gg) for gg in gt )
            else:
                gt = latexWord(gt)
            r += " & ".join([ latexWord(x) for x in observation ] + [latexWord(ur),gt])
            r += "\\\\\n"
    r += "\\bottomrule\\end{longtable}"

    if isinstance(solution,Frontier): solution = solution.MAP(universal)
    rules = solution.rules
    B = FeatureBank([w for ws in problem.data for w in (ws if isinstance(ws,(list, tuple)) else [ws]) if w])
    r += '''\n\\begin{tabular}{l}\\emph{Rules: }\\\\
%s
\\end{tabular}'''%("\\\\\\\\".join([ r.sharpenChange(B).latex() for r in rules if not r.doesNothing() ]))
    r = r.replace("palletized","palatalized")
    if problem.stressful: r = r.replace("highTone","stress")

    return r


    

def latexSolutionAndProblem(path):
    solution = loadPickle(path)
    if isinstance(solution,list): solution = solution[0]
    if isinstance(solution, list): return "(invalid solution)"

    print "From",path
    print solution

    # figure out which problem it corresponds to
    problem = None
    f = path.split('/')[-1][:-2]
    if f.startswith('alternation'):
        problem = alternationProblems[int(f.split('_')[-1]) - 1]
    elif f.startswith('matrix'):
        problemNumber = int(f.split('_')[-1])
        problem = MATRIXPROBLEMS[problemNumber]
    if problem == None:
        print "Could not find the problem for path",path
        assert False


    r = "\\emph{%s:}\\\\"%(problem.languageName.replace('-','--'))
    
    if problem.parameters == None:
        r += "\\begin{longtable}{%s}\\toprule\n"%("l"*len(solution.prefixes) + "|ll")
        r += " & ".join([ ("$\\varnothing$" if len(p) == 0 else latexWord(p)) + " $+$stem$+$ " + ("$\\varnothing$" if len(s) == 0 else latexWord(s))
                          for p,s in zip(solution.prefixes, solution.suffixes) ] + ["$\\hat{\\text{UR}}$","UR"])
        r += "\n\\\\ \\midrule\n"
        correctAnswer = {tuple(None if zz is None else Morph(zz)
                               for zz in ss): Morph(s)
                         for ss,s in GoldSolution.solutions[problem.key].underlyingForms.iteritems()}
        for observation in problem.data:
            ur = solution.underlyingForms.get(observation,None)
            if observation not in correctAnswer:
                import pdb; pdb.set_trace()
                
            r += " & ".join([ latexWord(x) for x in observation ] + [latexWord(ur),latexWord(correctAnswer[observation])])
            r += "\\\\\n"
        r += "\\bottomrule\\end{longtable}"

        if isinstance(solution,Frontier): solution = solution.MAP()
        rules = solution.rules

    elif "Numbers between" in problem.description:
        r += "\\begin{longtable}{%s}\\toprule\n"%("ll")
        r += " & ".join([ "Number","Surface form"])
        r += "\n\\\\ \\midrule\n"
        for j in range(len(problem.data)):
            r += str(problem.parameters[j]) + " & "
            r += latexWord(problem.data[j])
            r += "\\\\\n"
        r += "\\bottomrule\\end{longtable}"
        rules = [solution]

    elif "alternations" in problem.parameters:
        assert str(solution.__class__) == 'solution.AlternationSolution'
        
        r += "\\begin{longtable}{%s}\\toprule\n"%("ll")
        r += " & ".join([ "Surface form","UR"])
        r += "\n\\\\ \\midrule\n"
        for x in problem.data:
            r += latexWord(x) + "&"
            r += latexWord(solution.applySubstitution(Morph(x)))
            r += "\\\\\n"
        r += "\\bottomrule\\end{longtable}\n\n"
        r += "\\begin{longtable}{ll}\\toprule\n"
        r += "\\emph{The surface form...}&\\emph{Is underlyingly...}"
        r += "\n\\\\ \\midrule\n"
        for k,v in solution.substitution.iteritems():
            r += latexWord(k) + "&" + latexWord(v)
            r += "\\\\\n"
        r += "\\bottomrule\\end{longtable}\n\n"

        rules = solution.rules
        
        

    r += '''\n\\begin{tabular}{l}\\emph{Rules: }\\\\
%s
\\end{tabular}'''%("\\\\".join([ r.latex() for r in rules if not r.doesNothing() ]))
    for ts in problem.solutions:
        rules = parseSolution(ts).rules
        r += '''\n\\begin{tabular}{l}\\emph{Textbook solution rules: }\\\\
%s
\\end{tabular}'''%("\\\\".join([ r.latex() for r in rules ]))
    return r

def latexFeatures(fm):
    features = list({f for _,v in fm.iteritems() for f in v
                    if not f in  ['syllableBoundary','wordBoundary']})
    n = len(features)
    r = "\\begin{longtable}{%s}\\toprule\n"%("c|" + "l"*len(features))
    r += "&".join([""] + [featureAbbreviation.get(f,f) for f in features])
    r += "\n\\\\ \\midrule\n"
    for p,fs in fm.iteritems():
        if latexWord(p) in ['\\textipa{\\~\\"u}','\\textipa{\\~\\"o}'] or \
           p in ['syllableBoundary','wordBoundary']: continue
        if '##' in latexWord(p): continue
        
        
        r += " & ".join([latexWord(p)] + \
                        [ "$+$" if f in fs else "$-$" for f in features ])
        r += "\\\\\n"
    r += "\\bottomrule\\end{longtable}"
    print r
    return r
    
LATEXPRELUDE = '''
\\documentclass{article}
\\usepackage[margin = 0.1cm]{geometry}
\\usepackage{verbatim}
\\usepackage{tipa}
\\usepackage{booktabs}
\\usepackage{amssymb}
\\usepackage{longtable}
\\usepackage{phonrule}
\\usepackage{color}
\\definecolor{observationColor}{RGB}{88,80,141}%{188,80,144}
%#003f5c 0,63,92
%#58508d 88,80,141
%#bc5090 188,80,144
%#ff6361 255,99,97
%#ffa600 255,166,0
%#003f5c 0,63,92
%#7a5195 122,81,149
%#ef5675 239,86,117
%#ffa600
%\\definecolor{languageColor}{RGB}{0,128,102}
\\definecolor{languageColor}{RGB}{0,63,92}
%\\definecolor{lexiconColor}{RGB}{51,76,128}
\\definecolor{lexiconColor}{RGB}{0,63,92}%
%\\definecolor{universalColor}{RGB}{255,128,128}
\\definecolor{universalColor}{RGB}{255,99,97}

\\begin{document}



'''

LATEXTUTORIAL = '''
\\textbf{Allophony problems} are given as a set of surface forms along with a set of pairs of phonemes. The goal of the student (as well as the goal of the model) is to recover rule(s) which predicts which element of each pair is the underlying form.
Model outputs for alternation problems are of the form:
\\begin{longtable}{ll}\\toprule
Surface form & UR
\\\\ \\midrule
\\emph{a given surface form}&\\emph{model's predicted underlying form}\\\\
\\multicolumn{2}{c}{$\\cdots$}\\\\
\\bottomrule\\end{longtable}
\\begin{longtable}{ll}\\toprule
\\emph{The surface form...}&\\emph{Is underlyingly...}
\\\\ \\midrule
\\emph{a phoneme}&\\emph{phoneme}\\\\
\\bottomrule\\end{longtable}
Followed by a sequence of rules output by the model.

\\vspace{2cm}

\\textbf{Non-allophony problems} are given as a matrix of surface forms, where the columns range over different inflections and the rows range over different stems. Missing data is notated with a dash ($-$). 
We show the model's predicted concatenative morphology in the first row of each such matrix.
In the penultimate column of each matrix we show the predicted underlying stems, and in the final column of each matrix we show the ground truth annotations.
After each such matrix we show the rules output by the model.
For example,
\\begin{longtable}{ll|ll}\\toprule
\\color{universalColor}{stem} & \\color{universalColor}{stem$+$\\textipa{i}} & \\^{UR} & UR
\\\\ \\midrule
\\color{observationColor}{\\textipa{klup}} & \\color{observationColor}{\\textipa{klubi}} & \\color{universalColor}{\\textipa{klub}} & \\textipa{klub}\\\\
\\color{observationColor}{\\textipa{trup}} & \\color{observationColor}{\\textipa{trupi}} & \\color{universalColor}{\\textipa{trup}} & \\textipa{trup}\\\\
\\multicolumn{2}{c}{$\\cdots $}&\\multicolumn{2}{|c}{$\\cdots $}\\\\
\\bottomrule\\end{longtable}
\\noindent illustrates a problem with two inflections, where the input to the model is the data colored {\\color{observationColor}{purple}}, from which it synthesizes the morphology and stems in {\\color{universalColor}{salmon}}, which should be compared with the ground truth annotation in black.
\\pagebreak

'''

LATEXEPILOGUE = '''

\\end{document}
'''

def exportLatexDocument(source, path):
    print(source)
    with open(path,'w') as handle:
        handle.write(LATEXPRELUDE + source + LATEXEPILOGUE)
    if '/' in path: directory = "/".join(path.split("/")[:-1])
    else: directory = "."
    #os.system('pdflatex %s -output-directory %s'%(path,directory))

if __name__ == "__main__":
    from fragmentGrammar import *
    import argparse
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument("--universal","-u",default=None)
    parser.add_argument("--checkpoints", nargs="+")                        
    arguments = parser.parse_args()

    sources = []
    
    universal = arguments.universal
    if universal is not None:

        universal = loadPickle(universal)
        #import pdb; pdb.set_trace()
        
        #universal = FragmentGrammar(universal)
        if len(arguments.checkpoints) == 0:
            for l,t,f in universal.fragments:
                l = str(l).replace("rule.","").replace("Guard","Trigger").replace("Specification","FeatureMatrix")
                print "%s::=&%s\\\\"%(l,f.latex())
    for idx,ck in enumerate(arguments.checkpoints):
        result = loadPickle(ck)
            
        if isinstance(result, AlternationSolution):
            name = ck.split('/')[-1].replace("_ug","").replace("_simple","").replace(".p","").replace("_ablation","")
            problem = Problem.named[name]
            sources.append(latexAlternation(result, problem))
        else:
            print(ck)
            sources.append(latexMatrixProblem(result))
            continue
        
            print(latexMatrix(Problem.named[result.problem].data))
            ff = result.finalFrontier
            for prefix, suffix in zip(ff.prefixes, ff.suffixes):
                if len(prefix) == 0:
                    print "stem+\\textipa{%s}"%latexWord(suffix),
                elif len(suffix) == 0:
                    print "\\textipa{%s}+stem"%latexWord(prefix),
                else:
                    print "\\textipa{%s}+stem+\\textipa{%s}"%(latexWord(prefix),latexWord(suffix)),
                print " $\\sim$ ",

            for ri,f in enumerate(ff.frontiers):
                print("Rule %d"%ri)
                for r in f:
                    print(r)
                    print(r.latex())
            print(ff)
            if arguments.universal:
                print("Here is the solution according to the universal grammar you provided:")
                s = ff.MAP(universal)
                for r in s.rules:
                    print r.latex()
            for _,uf in ff.underlyingForms.iteritems():
                print latexWord(uf),"\\\\"
    
    #latexFeatures(simpleFeatureMap)
    
    source = "\n\n\\pagebreak\n\n".join(sources)
    exportLatexDocument(source,"allTheSolutions.tex")
    os.system("pdflatex allTheSolutions.tex")

    
            

        
