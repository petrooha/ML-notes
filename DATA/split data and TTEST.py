import numpy
import scipy.stats
import pandas

def compare_avgs():
    ##performs a t-test on 2 sets of baseball data (lef and right handed hitters
    ff = pandas.read_csv(filename)
    ll = ff[ff['handedness'] == 'L']
    rr = ff[ff['handedness'] == 'R']
    #splits data into 2 dataframes with left and right handed bitters

    result = scipy.stats.ttest_ind(ll['avg'], rr['avg'], equal_var=False)
    #performs ttest
    if result[1] <=.05:#p-value is less than 5%
        return (False, result)
    else:
        return (True, result)
