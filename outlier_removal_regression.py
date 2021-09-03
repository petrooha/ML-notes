#!/usr/bin/python

import random
import numpy
import matplotlib.pyplot as plt
import pickle
import pandas as pd



### load up some practice data with outliers in it
ages = pickle.load( open("practice_outliers_ages.pkl", "r") )
net_worths = pickle.load( open("practice_outliers_net_worths.pkl", "r") )



### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
from sklearn.cross_validation import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

### fill in a regression here!  Name the regression object reg so that
### the plotting code below works, and you can see what your regression looks like

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(ages_train, net_worths_train)


try:
    plt.plot(ages, reg.predict(ages), color="blue")
except NameError:
    pass
plt.scatter(ages, net_worths)
plt.show()


### identify and remove the most outlier-y points
from sklearn.metrics import accuracy_score

cleaned_data = []

predictions = reg.predict(ages_train)


nt = list()
for sublist in net_worths_train:
    for item in sublist:
        nt.append(item)

at = list()
for sublist in ages_train:
    for item in sublist:
        at.append(item)

errors = list()

pp = list()
for sublist in predictions:
    for item in sublist:
        pp.append(item)
    
errs = list()
for s in range (0, len(pp)):
    r=(pp[s] - nt[s])**2
    errs.append(r)
    
for s in range (0, len(predictions)):
    d=tuple()
    d = d + (at[s],)
    d = d + (nt[s],)
    d = d + (errs[s],)
    errors.append(tuple(d))

g= (len(pp)*9/10)
lst = pd.Series(errs)
i = lst.nsmallest(g)
i = i.index

cd = list()
for s in range (0, len(i)):
    c= i[s]
    cd.append(errors[c])# data in format of list of tuples of (ages, nw, error)

ages=list()
for item in i:
    ages.append(ages_train[item])
net_worths=list()
for item in i:
    net_worths.append(net_worths_train[item])

reg.fit(ages, net_worths)
plt.plot(ages, reg.predict(ages), color="blue")

plt.scatter(ages, net_worths)
plt.xlabel("ages")
plt.ylabel("net worths")
plt.show()
print reg.coef_


"""
### only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    ### refit your cleaned data!
    try:
        reg.fit(ages, net_worths)
        plt.plot(ages, reg.predict(ages), color="blue")
    except NameError:
        print "you don't seem to have regression imported/created,"
        print "   or else your regression object isn't named reg"
        print "   either way, only draw the scatter plot of the cleaned data"
    plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()


else:
    print "outlierCleaner() is returning an empty list, no refitting to be done"
"""
