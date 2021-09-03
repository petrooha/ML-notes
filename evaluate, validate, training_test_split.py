#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

from time import time
import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )
from sklearn.model_selection import train_test_split
import numpy as np

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
### your code goes here 

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()

t0 =time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 =time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

print accuracy_score(pred, labels_test)
print precision_score(pred, labels_test)
print recall_score(pred, labels_test)

p = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
t = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print precision_score(t,p)


