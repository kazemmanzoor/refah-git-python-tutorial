def par(listA , lsitB):
    r = mEmpty(listA , listB)
    for i in range(len(lsitA)):
     for j in range(len(listB[0])):
       for k in range(len(listB)):
            r[i][j] += listA[i][k] * listB[k][j]
    return r


def mEmpty(a , b):
    listR = []
    rows = len(a)
    cols = len(b[0])
    new = [0]*cols
    for i in range(0 , rows):
        listR.append(new)
    return listR



