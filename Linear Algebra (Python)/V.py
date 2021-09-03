import numpy as np
from numpy.linalg import inv
from math import sqrt
from math import degrees
from numpy import arccos

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,1],[1,1]])

C = np.array([[2],[2]])

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
        for j in range(len(self[i])):
            a= a + self[i][j] **2
    return sqrt(a)

def normal_vector(self):
    m = magnitude(self)
    for i in range(len(self)):
        for j in range(len(self[i])):
            self[i][j] = self[i][j] / m
    return self

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

J = np.array([[8.462],[7.893],[-8.187]])
K = np.array([[6.984],[-5.975],[4.778]])
H = np.array([[-8.987],[-9.838],[5.031]])
G = np.array([[-4.268],[-1.861],[-8.866]])
F = np.array([[1.5],[9.547],[3.691]])
S = np.array([[-6.007],[0.124],[5.772]])

def area(a,b):
    return magnitude(cross(a,b))
A = np.array([[1,2,3],[4,0,6],[7,8,9]])
print magnitude(A)
