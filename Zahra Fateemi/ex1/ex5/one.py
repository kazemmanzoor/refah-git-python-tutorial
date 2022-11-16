def Func(a):
    list = []
    for item in a:
        count = 0
        for i in item:
            count = count+i
        list.append(count)
    return list

list = [[2,4,5],[3,6,1]]
print(Func(list))
