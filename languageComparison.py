from utilities import *
from matrix import *
from problems import *
from textbook_problems import *
from parseSPE import parseSolution

import matplotlib.pyplot as plot



class SolutionAnalysis(object):
    def __init__(self, language, mySolution, textbookSolution):
        self.language = language
        self.mySolution = mySolution
        self.textbookSolution = textbookSolution

    def relativeLogLikelihood(self):
        if isinstance(self.mySolution, AlternationSolution):
            assert isinstance(self.textbookSolution, AlternationSolution)
            return 1.
        assert len(self.mySolution.underlyingForms) == len(self.textbookSolution.underlyingForms)
        return float(sum(len(s) for s in self.textbookSolution.underlyingForms.values() )) \
            / float(sum(len(s) for s in self.mySolution.underlyingForms.values() ))

    @property
    def ranking(self):
        return self.relativeLogLikelihood()


def analyzeSolution(path):
    solution = loadPickle(path)
    if isinstance(solution,list): solution = solution[0]
    if isinstance(solution, list): return "(invalid solution)"
    if isinstance(solution.underlyingForms, list):
        # Legacy pickles
        solution.underlyingForms = {}

    print "From the path",path,"the following solution was "
    print solution

    # figure out which problem it corresponds to
    problem = None
    f = path.split('/')[-1][:-2]
    if f.startswith('alternation'):
        problem = alternationProblems[int(f.split('_')[-1]) - 1]
    elif f.startswith('matrix'):
        problemNumber = int(f.split('_')[-1])
        if problemNumber < 50: problem = underlyingProblems[problemNumber - 1]
        elif problemNumber < 70: problem = interactingProblems[problemNumber - 50 - 1]
        elif problemNumber < 80: problem = sevenProblems[problemNumber - 70 - 1]
    if problem == None:
        print "Could not find the problem for path",path
        assert False

    # matrix problem
    if problem.parameters is None or "Numbers between" in problem.description:
        textbookSolution = parseSolution(problem.solutions[0])
        if problem.parameters is None:
            solver = UnderlyingProblem(problem.data)
            solution = solver.solveUnderlyingForms(solution)
            textbookSolution = solver.solveUnderlyingForms(textbookSolution)
        else:
            # Tibetan counting problem
            # The textbook underlying forms are the same as the one that we find
            textbookSolution.underlyingForms = solution.underlyingForms
    elif "alternations" in problem.parameters:
        assert str(solution.__class__) == 'solution.AlternationSolution'
        textbookSolution = solution

    return SolutionAnalysis(problem.languageName,
                            mySolution = solution,
                            textbookSolution = textbookSolution)

if __name__ == "__main__":
    analyses = [ analyzeSolution("pickles/alternation_%d.p"%j)
                 for j in range(1,11+1) ] + \
                     [ analyzeSolution("pickles/matrix_%d.p"%j)
              for j in range(1,15+1) + [51,52,53,55] ]
               
                # + []
                # [ analyzeSolution("pickles/matrix_%d.p"%j)
                #   for j in [51,52,53,55] ]

    # Order the analyses by how successful they were
    analyses.sort(key = lambda a: a.ranking, reverse = True)

    # Name them appropriately if there are duplicated languages
    Latin = ['I','II','III']
    for j,a in enumerate(analyses):
        a.languageLabel = a.language
        if sum(b.language == a.language for b in analyses) > 1:
            k = 0
            for b in analyses[:j]:
                if b.language == a.language: k += 1
            a.languageLabel += " (%s)"%(Latin[k])            
    
    ys = range(len(analyses))
    plot.barh(ys,
              [a.relativeLogLikelihood() for a in analyses ],
              0.7)
    plot.gca().set_yticks(ys)
    plot.gca().set_yticklabels([ a.languageLabel for a in analyses ])
    plot.gca().set_xlabel('% compression relative to textbook solution')
    plot.show()
