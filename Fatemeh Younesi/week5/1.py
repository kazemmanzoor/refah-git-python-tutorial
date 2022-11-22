def myFunc(a):
    listSum = []
    for item in a:
        count = 0
        for i in item:
            count = count+i
        listSum.append(count)
    return listSum
