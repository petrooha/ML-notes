#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#####################


clf = DecisionTreeClassifier(min_samples_split = 40)
# min_samples_split sets the amount of nodes in a desicion tree where it should stop splitting it (the higher the number - the less overfitting) by default its 2

t0 =time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 =time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

print accuracy_score(pred, labels_test)

#### CODE TO COMPARE ACCURACY IN DIFFERENT min_samples_split  ###
"""
clf = tree.DecisionTreeClassifier(min_samples_split=2)
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc_min_samples_split_2 = accuracy_score(pred, labels_test)

clf2 = tree.DecisionTreeClassifier(min_samples_split=50)
clf2 = clf2.fit(features_train, labels_train)
pred2 = clf2.predict(features_test)
acc_min_samples_split_50 = accuracy_score(pred2, labels_test)


def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}
          """

