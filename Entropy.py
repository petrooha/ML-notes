import scipy.stats
def ent(x, y):
    print scipy.stats.entropy([x, y-x],base=2) 
