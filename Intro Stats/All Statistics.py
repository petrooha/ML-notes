import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import random
from math import sqrt

################    Graphs    ###############

#plt.scatter
#plt.bar
#plt.hist(values,bins=20)


#plt.show()


#############   Bayes Rule   ####################

#Return the probability of A conditioned on B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 

"""p1 is sensetivity
p2 is specitivity"""

def P(p0,p1,p2):
    pB=p0*p1 + (1-p0)*(1-p2)
    pAonB=p0*p1/pB

    pnB=p2*(1-p0) + (1-p1)*p0
    pAnB=p0*(1-p1)/pnB
    print("P(B) = "+str(pB))
    print("P(not B) = "+str(pnB))
    print("P(A conditioned on B) = "+str(pAonB))
    print("P(A conditioned on Not B) = "+str(pAnB))

####################


def mean(data):
    return 1.0 * sum(data) / len(data)

def median(data):
    sd=sorted(data)
    if len(sd)%2==0:
        return (1.0*sd[len(sd)/2] + 1.0*sd[len(sd)/2 -1])/2
    else:
        return sd[len(sd)/2]

def mode(data):
    m=[data[0]]
    c=1
    
    for e in data:
        if data.count(e)>c:
            m=[e]
            c=data.count(e)
        elif data.count(e)>1 and data.count(e)==c and e not in m:
            m.append(e)
    if c==1:
        return "No mode"
    else:
        return m

def variance(data):
    v=0
    m=mean(data)
    for e in data:
        v=v+(m-e)**2
    return v / len(data)

def stdev(data):
    return (variance(data))**0.5

def Zscore(n, data):#n is value of the set
    return (n - mean(data)) / stdev(data) #returns Z-score

def zscore(data, z):#doesnt produce z but the value with given z
    return z*stdev(data) + mean(data)

def quart(data):
    d=[]
    sd=sorted(data)
    if len(data)%4==0:
        for e in range(len(sd)/4 ,len(sd)*3/4):
            d.append(sd[e])
    else:
        for e in range(len(sd)/4 ,len(sd)*3/4 + 1):
            d.append(sd[e])
    return d
#this is Sebastian's way of calculating Quartiles (same result):
def quart2(data):
    d=[]
    sd=sorted(data)
    qb=(len(sd)-3)/4
    qe=qb*3+3
    for e in range(qb,qe):
        d.append(sd[e])
    return d

def conf(l):
    return 1.96 * ((variance(l) / len(l))**.5)
# also I saw them computing it as "1.96*(mean-stdev) to 1.96(mean+stdev)"

def ci(data):
    print mean(data) + conf(data)
    print mean(data) - conf(data)

def test(l, h):#hypothesis test
    if h>(mean(l)+conf(l)) or h<(mean(l)-conf(l)):
        return False
    else:
        return True

############ Regression & Correlation  ####################
def covariance(x,y):
    xys=0
    for e in range(0,len(x)):
        xys=xys+(x[e]-mean(x))*(y[e]-mean(y))
    return xys/len(x)

def reg(x,y):
    xys=0
    xxs=0
    yys=0
    for e in range(0,len(x)):
        xys=xys+(x[e]-mean(x))*(y[e]-mean(y))
    for i in x:
        xxs=xxs+(i-mean(x))**2
    for j in y:
        yys=yys+(j-mean(y))**2

    return xys/((xxs*yys)**0.5)

def cor(x,y):
    return covariance(x,y) / (stdev(x)*stdev(y))

#######       Regression line  y=Bx + A 
def B(x,y):
    return covariance(x,y) / variance(x)
    """         OR:
    xys=0
    xxs=0
    yys=0
    for e in range(0,len(x)):
        xys=xys+(x[e]-mean(x))*(y[e]-mean(y))
    for i in x:
        xxs=xxs+((i-mean(x))**2)
    return xys/xxs
    """
def A(x,y):
    return mean(y) - B(x,y)*mean(x)

############       By the way:
"""Zscore(x) = (x[i] - mean(x)) / stdev(x)
same for y
B / reg = stdev(y) / stdev(x)"""
