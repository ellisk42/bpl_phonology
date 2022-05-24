import time

class Result:
    def __init__(self, problem):
        self.parameters = None
        self.problem = problem
        self.finalFrontier = None
        self.solutionSequence = []
        self.startTime = time.time()

    def recordSolution(self, solution):
        self.solutionSequence.append((solution, time.time() - self.startTime))

    def recordFinalFrontier(self, frontier):
        assert self.finalFrontier is None
        self.finalFrontier = frontier

    def lastSolutionIsFinal(self):
        if len(self.solutionSequence) == 0:
            print "warning: lastSolutionIsFinal called without a final solution. ignoring..."
            return
        self.recordFinalFrontier(self.solutionSequence[-1][0].toFrontier())

        return self
