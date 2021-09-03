import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys

def compute_r_squared(data, predictions):
    tss = 0
    rss = 0
    for i in range(0,len(data)):
        rss = rss + (data[i] - predictions[i])**2
        tss = tss + (np.mean(data) - data[i])**2
        
    r_squared = (tss-rss)/tss
    return r_squared
