import numpy as np
from numpy.linalg import inv

def update(mean1, var1, mean2, var2):
    new_mean = (1/(var1 + var2))*(var1*mean2 + var2*mean1)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range(len(motion)):
    mu, sig = update(mu, sig, measurements[i], measurement_sig)
    #print mu, sig

    mu, sig = predict(mu, sig, motion[i], motion_sig)
    #print mu, sig

########################################

#######################################
# Implement the filter function below

def kalman_filter(x, P):
    for n in range(len(measurements)):

        #prediction update
        x  = np.dot(F, x) + u
        print x
        print "================="
        P = np.dot(F, np.dot(P, np.transpose(F)))
        print np.transpose(F)
        print "--------"
        print np.dot(P, np.transpose(F))
        print "--------"
        print P
        print "===================="
        
        # measurement update
        Z = np.array([measurements[n]])
        Y = np.transpose(Z) - np.dot(H, x)
        print Z
        print "---------"
        print H
        print "---------"
        print x
        print "---------"
        print np.dot(H, x)
        print "================"
        K1 = np.dot(P, np.transpose(H))
        S = np.dot(H, np.dot(P, np.transpose(H))) + R
        K = np.dot(K1, inv(S))
        print P
        print "---------"
        print np.transpose(H)
        print "---------"
        print K1
        print "---------"
        print S
        print "---------"
        print K
        print "================="
        x = x + np.dot(K, Y)
        P = np.dot((I - np.dot(K, H)), P)
        print Y
        print "---------"
        print x
        print "---------"
        print np.dot(K,H)
        print "---------"
        print P
        print "---------"
        print "---------"
        

    return x, P

################################
measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]

initial_xy = [4., 12.]
dt = 0.1

x = np.array([[initial_xy[0]], [initial_xy[1]], [0.], [0.]]) # initial state (location and velocity)
u = np.array([[0.], [0.], [0.], [0.]]) # external motion

P = np.array([[0., 0., 0., 0.],[0., 0., 0., 0.],[0., 0., 1000., 0.],[0., 0., 0., 1000.]])#initial uncirtainty, for x_y is 0, for velocity is 1000
F = np.array([[1., 0., dt, 0.],[0., 1., 0., dt],[0., 0., 1., 0.],[0., 0., 0., 1.]])
H = np.array([[1., 0., 0., 0.],[0., 1., 0., 0.]])# projection for 4 dimensions to 2 dimensions (x_y but not velocities)
R = np.array([[0.1, 0.],[0., 0.1]])# 2x2 with 0.1 diagonal
I = np.identity(4)

############################################
### use the code below to test your filter!
############################################
"""
measurements = [1, 2, 3]

x = np.array([[0.], [0.]]) # initial state (location and velocity)
P = np.array([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = np.array([[0.], [0.]]) # external motion
F = np.array([[1., 1.], [0, 1.]]) # next state function
H = np.array([[1., 0.]]) # measurement function
R = np.array([[1.]]) # measurement uncertainty
I = np.array([[1., 0.], [0., 1.]]) # identity matrix
"""
print(kalman_filter(x, P))
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]

