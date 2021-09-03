import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import random
from math import sqrt


def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))
    
def flip(N):
    f=[]
    for e in range(0,N):
        a = random.randint(0,1)
        f.append(a)
    return f
    
def sample(N):
    outcomes=[]
    for e in range(0,N):
        outcomes.append(mean(flip(N)))
    return outcomes
#change N and bins-->
N=100
outcomes=sample(N)
plt.hist(outcomes,bins=20)
plt.show()

print mean(outcomes)
print stddev(outcomes)
