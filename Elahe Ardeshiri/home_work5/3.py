a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

def EmptyMatrix(x , y):
    listResult = []
    rows = len(x)
    cols = len(y[0])
    newcols = [0]*cols
    for i in range(0 , rows):
        listResult.append(newcols)
    return listResult

def fun(A , B):
    result = makeMatrix(A , B)
    for i in range(len(A)):
     for j in range(len(B[0])):
       for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
    return result

print(fun(a , b))
