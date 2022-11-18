def myFunc(a):
    listSum = []
    for item in a:
        count = 0
        for i in item:
            count = count+i
        listSum.append(count)
    return listSum



#--------------------------------------------------------
mylist = [[2,4,5],[12,5,90],[3,43,1]]
print(myFunc(mylist))
