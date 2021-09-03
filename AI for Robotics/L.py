from decimal import Decimal, getcontext
import numpy as np
from numpy.linalg import inv
from math import sqrt
from math import degrees
from numpy import arccos


######################

def plus(self, v):
    if len(self)>= len(v) and len(self[0])>=len(v[0]):
        a = np.zeros([len(self),len(self[0])])
    elif len(self)>=len(v) and len(self[0])<=len(v[0]):
        a = np.zeros([len(self),len(v[0])])
    elif len(self)<=len(v) and len(self[0])>=len(v[0]):
        a = np.zeros([len(v),len(self[0])])
    else:
        a = np.zeros([len(v),len(v[0])])
    for i in range(len(self)):
        for j in range(len(self[i])):
            a[i][j] = a[i][j] + self[i][j]
    for i in range(len(v)):
        for j in range(len(v[i])):
            a[i][j] = a[i][j] + v[i][j]
    return a
     
def magnitude(self):
    a=0
    for i in range(len(self)):
        for j in range(len(self[0])):
            a= a + self[i][j] **2
    return sqrt(a)

def normal_vector(self):
    m = magnitude(self)
    temp = np.zeros([len(self),len(self[0])])
    for i in range(len(self)):
        for j in range(len(self[0])):
            a =  self[i][j]/m
            temp[i][j] = temp[i][j] + a
    return temp

def dot_product(self, v):
    a=0
    for i in range(len(self)):
        for j in range(len(self[i])):
            a= a+self[i][j]*v[i][j]
    return a

def radiant(self, v):
    theta = arccos(dot_product(self, v)/(magnitude(self)*magnitude(v)))
    return theta

def degree(self, v):
    return degrees(radiant(self, v))

def is_zero(self, tolerance=1e-10):
        return magnitude(self) < tolerance

        #Projection
def proj_parallel(self, basis):
    u = normal_vector(basis)
    uv = dot_product(self, u)
    return u*uv

def proj_orthagonal(self, basis):
    proj = proj_parallel(self, basis)
    return self - proj

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

###################


def first_nonzero_index(iterable):
    eps=1e-10
    for k, item in enumerate(iterable):
        if not (item)<eps:
            return k
    raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(float):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

def is_parallel(self, v):
    if abs(degree(self, v) - 180) < 2 or abs(degree(self, v)) < 2:
        return True

def is_eq(self, v):
    nz = int(v[first_nonzero_index(v)])
    x = float(self[0] / v[0])
    for i in range(len(self) - 1):
        if abs(x - float(self[i] / v[i])) > 0.003:
            return "Not Parallel"#, degree(self, v), intersection(self,v)
    if abs(x - float(self[-1] / v[-1])) < 0.003:
        return "Equal"
    else:
        return "Parallel"

def intersection(self, v):
    A, B = normal_vector(self)[0:2]
    C,D = normal_vector(v)[0:2]
    k1 = self[2]
    k2 = v[2]
    x_numerator = D*k1 - B*k2
    y_numerator = -C*k1 + A*k2
    denominator = A*D - B*C
    return np.array([[x_numerator/denominator, y_numerator/denominator]])

A = np.array([[1,2,3],[4,0,6],[7,8,9]])
J = np.array([[0],[7.893],[-8.187]])

#### calling rows columns and cells##
###############
print A[1][2]##
print A[1]   ##
print A[:,2] ##
###############
###############
B=np.array([[-0.412], [3.806], [0.728],[-3.46]])
C=np.array([[1.03],[-9.515], [-1.82],[8.65]])


K = np.array([[2.611],[5.528],[0.283],[4.6]])
H = np.array([[7.715],[8.306],[5.342],[3.76]])

G = np.array([[-7.926],[8.625],[-7.217],[-7.952]])
F = np.array([[-2.642],[2.875],[-2.404],[-2.443]])

S = np.array([[-6.007],[0.124],[5.772]])


#######################################

