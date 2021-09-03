from math import sqrt
from math import degrees
from numpy import arccos
import numpy as np

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

def plus(self, v):
    new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
    #new_coordinates = []
    #n = len(self.coordinates)
    #for i in range(n):
    #    new_coordinates.append(self.coordinates[i] + v.coordinates[i])
    return Vector(new_coordinates)

def minus(self, v):
    new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)

def times_scaler(self, v):
    new_coordinates = [self*v for self in self.coordinates]
    return Vector(new_coordinates)
"""
A = Vector([8.218, -9.341])
B = Vector([-1.129, 2.111])
C = Vector([7.119, 8.215])
D = Vector([-8.223, 0.878])
E = Vector([1.671, -1.012, -0.318])
print plus(A, B)
print minus(C, D)
print times_scaler(E, 7.41)
"""
def mag(self):
    a=0
    for i in range(len(self.coordinates)):
        a = a + self.coordinates[i]**2
    return sqrt(a)
"""
F = Vector([-0.221, 7.437])
print "magnitude of ", F, " is ", mag(F)
G = Vector([8.813, -1.331, -6.247])
print "magnitude of ", G, " is ", mag(G)
"""
def norma(self):
    m = mag(self)
    a = [self / m for self in self.coordinates]
    return Vector(a)
"""
H = Vector([5.581, -2.136])
J = Vector([1.996, 3.108, -4.554])
print "normalized ", H, " is ", norma(H)
print "normalized ", J, " is ", norma(J)
"""
def times(self, v):
    ans = sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    return ans

def radiant(self, v):
    theta = arccos(times(self, v)/(mag(self)*mag(v)))
    return theta

def degree(self, v):
    return degrees(radiant(self, v))


"""
O = Vector([3.183, -7.627])
P = Vector([-2.668, 5.319])
print "Theta of ", O, " and ", P, " is ", radiant(O, P), " radians."

R = Vector([7.35, 0.221, 5.188])
S = Vector([2.751, 8.259, 3.985])
print "Theta of ", R, " and ", S, " is ", degree(R, S), " degrees."
"""
def comp_parallel(self, basis):
    u = norma(basis)
    uv = times(self, u)
    return times_scaler(u, uv)

def comp_orthagonal(self, basis):
    proj = comp_parallel(self, basis)
    return minus(self, proj)
"""
T = Vector([3.039, 1.879])
Q = Vector([0.825, 2.036])
print comp_parallel(T, Q)
K = Vector([-9.88, -3.264, -8.159])
L = Vector([-2.155, -9.353, -9.473])
print comp_orthagonal(K,L)
V = Vector([3.009, -6.172, 3.692, -2.51])
W = Vector([6.404, -9.144, 2.759, 8.718])
print comp_parallel(V,W) + comp_orthagonal(V,W)
"""
def crossproduct(self, v):
    x1, y1, z1 = self.coordinates
    x2, y2, z2 = v.coordinates
    ans = [y1*z2 - z1*y2, x2*z1 - x1*z2, x1*y2 - x2*y1]
    return Vector(ans)
J = Vector([8.462,7.893,-8.187])
K = Vector([6.984,-5.975,4.778])
