from problems import MATRIXPROBLEMS, alternationProblems

from utilities import *
import pickle
import os
import sys

def numberOfCPUs():
    import multiprocessing
    return multiprocessing.cpu_count()


def flushEverything():
    sys.stdout.flush()
    sys.stderr.flush()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "Curriculum solving of phonology problems. Calls out to UG.py and driver.py")
    parser.add_argument("startingIndex",
                        type=int,
                        help="Which problem to start out solving. 0-indexed")
    parser.add_argument("endingIndex",
                        type=int)
    parser.add_argument("ug",
                        choices=["empirical","ground","none"],
                        help="What kind of universal grammars to use. empirical: estimate from solutions found to previous problems. ground: estimate using textbook solutions. none: do not use universal grammar.")
    parser.add_argument("--CPUs",
                        type=int,
                        default=None)
    parser.add_argument("--timeout",
                        type=float,
                        default=None)
    parser.add_argument("--serial",
                        default=False,
                        action="store_true")
    parser.add_argument("--visualize",
                        type=str,
                        default=None)
    
    arguments = parser.parse_args()
    def universal(j):
        if arguments.ug == "none":
            u = ""
        elif arguments.ug == "empirical":
            u = "--universal universalGrammars/empirical_%d.p"%j
        elif arguments.ug == "ground":
            u = "--universal universalGrammars/groundTruth_%d.p"%j
        else: assert False
        return u

    if arguments.ug == "ground":
        pickleDirectory = "frontierPickles/groundUniversal"
    elif arguments.ug == "none":
        pickleDirectory = "frontierPickles/noUniversal"
    elif arguments.ug == "empiricalUniversal":
        pickleDirectory = "frontierPickles/empiricalUniversal"
    else: assert False
    pickleArgument = " --pickleDirectory %s/ "%pickleDirectory

    if arguments.visualize:
        import matplotlib.pyplot as plot
        
        covers = []
        for ap in alternationProblems:
            language = ap.languageName
            if ' (' in language:
                language = language[:language.index(' (')]
            covers.append((language + '*', 1.))
        
        for j in range(arguments.startingIndex, arguments.endingIndex+1):
            fn = '%s/matrix_%d.p'%(pickleDirectory,j)
            try:
                with open(fn,'rb') as handle:
                    solution = pickle.load(handle)
                    covered = len(solution.underlyingForms)
            except IOError:
                print "WARNING: Could not load",fn
                covered = 0
            total = len(MATRIXPROBLEMS[j].data)
            language = MATRIXPROBLEMS[j].languageName
            
            # Tibetan counting is weird
            if language == 'Tibetan': covered = total
                
            covers.append((language,covered/float(total)))
            print fn, language, covered/float(total)
        plot.figure(figsize=(5,10))
        plot.yticks(rotation=45)
        plot.barh(range(len(covers)),
                 [c for l,c in covers ],
                 tick_label=[l for l,c in covers ])
        plot.xlabel('% data covered by rules')

        if arguments.ug == "ground":
            plot.title("Learned UG (supervised)")
        elif arguments.ug == "none":
            plot.title("No UG")
        elif arguments.ug == "empirical":
            plot.title("Learned UG (unsupervised)")
        plot.tight_layout()
        plot.savefig(arguments.visualize)

        import sys
        sys.exit(0)
        


    if arguments.timeout is None: timeout = ""
    else: timeout = " --timeout %f"%arguments.timeout

    displayTimestamp("Curriculum training")
    CPUs = arguments.CPUs or numberOfCPUs()
    print("Using %d CPUs"%CPUs)

    os.system("python command_server.py %d &"%CPUs)

    if arguments.ug == "ground":
        print "Precomputing ground-truth universal grammars..."
        for j in xrange(arguments.startingIndex, arguments.endingIndex+1):
            os.system("pypy UG.py fromGroundTruth --CPUs %d --problems %d --export universalGrammars/groundTruth_%d.p"%(CPUs, j, j))

    if arguments.ug in ["ground","none"] and not arguments.serial:
        print "Launching all jobs in parallel!"
        import subprocess
        processes = [subprocess.Popen("python driver.py %d incremental --cores %d --top 100 %s %s %s" %
                                      (j, CPUs, pickleArgument, universal(j), timeout),
                                      shell=True)
                     for j in xrange(arguments.startingIndex, arguments.endingIndex+1)]
        for p in processes:
            p.wait()

    else:
        for j in xrange(arguments.startingIndex, arguments.endingIndex+1):
            print("Solving problem %d"%j)
            command = "python driver.py %d incremental --cores %d --top 100 %s %s %s"%(j,CPUs,
                                                                                      universal(j),
                                                                                      pickleArgument,
                                                                                      timeout)
            print
            print "\tCURRICULUM: Solving problem %d by issuing the command:"%j
            print "\t\t",command
            flushEverything()
            os.system(command)

            if arguments.ug == "empiricalUniversal":
                command = "pypy UG.py fromFrontiers --CPUs %d --problems %d --export universalGrammars/empirical_%d.p"%(CPUs, j, j)
                print
                print "Re- estimating universal grammar by executing:"
                print command
                os.system(command)


