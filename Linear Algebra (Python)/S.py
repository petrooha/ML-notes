import numpy as np


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
def swap_rows(self, row1, row2):
    if row2 > len(self):
        return "Many solutions"
    x = np.array(self[row2])
    self[row2]=self[row1]
    self[row1]=x
    return self

# he did normal vectors of next two, I leave it like this cuz it doesnt make sense
def multiply_coefficient_and_row(self, coefficient, row):
    self[row] = self[row]*coefficient
    return self


def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
    self[row_to_be_added_to] = self[row_to_add]*coefficient + self[row_to_be_added_to]
    return self


def indices_of_first_nonzero_terms_in_each_row(self):
    num_equations = len(self)
    num_variables = self.dimension

    indices = [-1] * num_equations

    for i,p in enumerate(self.planes):
        try:
            indices[i] = p.first_nonzero_index(p.normal_vector)
        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                continue
            else:
                raise e
    return indices

def tri(self):
    self = self*1.0
    nr = len(self)
    nc = len(self[0]) - 1
    for j in range(len(self[0])-1):
        for i in range(j+1,len(self)):
            if self[i][j] ==0:
                swap_rows(self, i, i+1)
            c = float((-1) * self[i][j] / self[j][j])
            add_multiple_times_row_to_row(self, c, j, i)

    for j in range(len(self[0] - 1)):
        for i in range(j+1,len(self)):
            c = float((-1) * self[len(self)-i-1][len(self[0])-2-j] / self[len(self[0])-2-j][len(self[0])-2-j])
            add_multiple_times_row_to_row(self, c, len(self[0])-2-j, len(self)-i-1)

    for i in range(len(self)):
        c = float(1 / self[i][i])
        self[i] = self[i]*c
        
    return self
Z = np.array([[1,2,3,4],[4,5,6,0],[7,8,3,-3]])
