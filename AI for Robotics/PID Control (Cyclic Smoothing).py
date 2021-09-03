from math import *


def smooth(path, weight_data = 0.1, weight_smooth = 0.1, tolerance = 0.00001):

    # 
    # Enter code here
    #
    # Make a deep copy of path into newpath
    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(len(path)):
            for j in range(len(path[0])):
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j]) + weight_smooth * (newpath[(i-1)%len(path)][j] + newpath[(i+1)%len(path)][j] - 2.0 * newpath[i][j])
                change += abs(aux - newpath[i][j])    
    return newpath

