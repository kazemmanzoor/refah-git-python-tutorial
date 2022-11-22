a1 = [[5, 8, 7],
     [6, 1, 5]]
b1 = [[7, -30, 22],
     [2, 10, 5],
     [15, 3, 2]]




def myFunc(A , B):
    result = makeEmptyMatrix(A , B)
    for i in range(len(A)):
     for j in range(len(B[0])):
       for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
    return result


def makeEmptyMatrix(a , b):
    listResult = []
    rows = len(a)
    cols = len(b[0])
    newlistcols = [0]*cols
    for i in range(0 , rows):
        listResult.append(newlistcols)
    return listResult
print(myFunc(a1 , b1))
