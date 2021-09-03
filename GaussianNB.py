import numpy as np

x = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])# features
y = np.array([1,1,1,2,2,2])# lables
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf = GaussianNB() # creating a classifier

clf.fit(x,y) # making it learn the pattern OR "training"

pred = clf.predict([[-0.8, -1]])# giving the feature and asking for the label OR "predicting"
print pred

#accuracy_score(pred, actual_label_for_set) => will produce the accuracy rate
"""
to measure the time it takes to run a function, for example,
to compare what takes longer training or prediction

t0 =time()
FUNCTION
print "training time:", round(time()-t0, 3), "s"

"""
