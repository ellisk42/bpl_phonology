import os
import matplotlib.pyplot as plot
import pickle

def loadAccuracies(model):
    pickles = [ "testingAccuracy/"+f for f in os.listdir("testingAccuracy") if f.endswith('.p') ]
    
    accuracies = {}
    compression = {}
    
    for p in pickles:
        record = pickle.load(open(p,"rb"))
        t = record['testing']
        accuracies[t] = accuracies.get(t,[]) + [record['accuracy'][model]]
        compression[t] = compression.get(t,[]) + [record['compression'][model]]
    return accuracies,compression

if __name__ == '__main__':
    for model in ['flat','learned','Chomsky']:
        a,c = loadAccuracies(model)
        print model
        print "accuracies:"
        for hold in sorted(a.keys()):
            print hold, sum(a[hold])/len(a[hold])
        print "compression:"
        for hold in sorted(c.keys()):
            print hold, sum(c[hold])/len(c[hold])
        print ""
