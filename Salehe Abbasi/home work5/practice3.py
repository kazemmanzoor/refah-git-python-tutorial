import numpy as np
def myFunc(A , B):
    result = np.zeros((len(A),len(B[0])))
    for i in range(len(A)):
     for j in range(len(B[0])):
       for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
    return result




#----------------------------------------------------
a1 = [[2, 3, 4],
     [3, 4, 5]]
b1 = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(myFunc(a1 , b1))
