import numpy as np

def test_run():
    # Empty array with random numbers
    print np.empty(5)
    print np.empty((5,4))# 5 rows 4 coumns
    print np.empty((5,4,3))# 3-dimentional array
    print np.ones((5,4))
    print np.random.random((5,4))# random #s between 0 and 1

    # Sample numbers from Guassian
    print np.random.normal(size=(2,3))# standars normal -> mean=0, s.d.=1
    print np.random.normal(50, 10, size=(2,3))# change mean to 50 and s.d. to 10    

    #Random Integers
    print np.random.randint(10) # asingle integer 0:10
    print np.random.randint(0, 10) # same as above, specifying [low, high] explicit
    print np.random.randint(0, 10, size=5) # 5 random integers as a 1D array
    print np.random.randint(0, 10, size=(2, 3)) # 2x3 array of rnadom integers

    # Array atributes
    a = np.random.random((5,4)) # 5x4 array
    print a.shape[0] # number of rows
    print a.shape[1] # number of columns
    print len(a.shape)# dimensions of array
    print a.size # number of elements (in 2D its rows*columns)

    # Seed the random number generator
    np.random.seed(369)
    a=np.random.randint(0, 10, size=(5,4))
    print "Array:\n", a

    # Mathematics
    print "Sum of each column:\n", a.sum(axis=0)
    print "Sum of each row:\n", a.sum(axis=1)
    print "Same for min, max, etc."

    a[a<a.mean()] = a.mean()# replace all values that < mean with mean
    print a, " prints mean instead of values that less than mean"

if __name__ == "__main__":
    test_run()
