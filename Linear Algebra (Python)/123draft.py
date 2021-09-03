
x2 = []

def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])

    return column

def dotproduct(vectora, vectorb):
    
    # variable for accumulating the sum
    result = 0
    
    # TODO: Use a for loop to multiply the two vectors
    # element by element. Accumulate the sum in the result variable
    for i in range(len(vectora)):
        result = result + vectora[i]*vectorb[i]
    
    return result
    
x2 = [dotproduct([8, 7, 12, 5], [1, 0, 2, 0]), 
      dotproduct([8, 7, 12, 5], [0, 1, 0, 2]),
      12,
      5]

### TODO: Write a function called matrix_multiplication that takes
###       two matrices,multiplies them together and then returns
###       the results
###       
###       Make sure that your function can handle matrices that contain
###       only one row or one column. For example,
###       multiplying two matrices of size (4x1)x(1x4) should return a
###       4x4 matrix

def matrix_multiplication(matrixA, matrixB):
    result = []

    for i in range(len(matrixA)):
        a1=matrixA[i]
        row_result=[]
        for j in range(len(matrixB[0])):
            b1=get_column(matrixB, j)
            dp = dotproduct(a1, b1)
            row_result.append(dp)
        result.append(row_result)
    return result
A=[[5],[2]]
B=[[5,1]]
print len(A)
print len(B)
print matrix_multiplication([[5], [2]], [[5, 1]]) == [[25, 5], [10, 2]]
print matrix_multiplication([[5, 1]], [[5], [2]]) == [[27]]
print matrix_multiplication([[4]], [[3]]) == [[12]]
print matrix_multiplication([[2, 1, 8, 2, 1], [5, 6, 4, 2, 1]], [[1, 7, 2], [2, 6, 3], [3, 1, 1], [1, 20, 1], [7, 4, 16]])# == [[37, 72, 33], [38, 119, 50]]
