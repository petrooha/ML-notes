
def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])

    return column

def dotproduct(vectora, vectorb):
    result = 0
    for i in range(len(vectora)):
        result = result + vectora[i]*vectorb[i]
    
    return result
    
def transpose(m):
    temp = []
    for i in range(len(m[0])):
        temp.append(get_column(m, i))
    return temp

# next two functions do same thing
def transpose_multiplication(matrixA, matrixB):
    newB = transpose(matrixB)
    result = []
    for i in range(len(matrixA)):
        temp = []
        for j in range(len(newB)):
            temp.append(dotproduct(matrixA[i], newB[j]))
        result.append(temp)
    return result

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

def identity_matrix(n):
    
    identity = []
    
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        temp[i] = 1
        identity.append(temp)

    return identity

print identity_matrix(2) == [[1, 0], 
                             [0, 1]]
