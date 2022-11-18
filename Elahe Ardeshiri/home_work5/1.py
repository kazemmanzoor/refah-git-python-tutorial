list1 = [[2,1,8],[7,81,21],[6,4,11]]

def fun(a):
    list2 = []
    for item in a:
        count = 0
        for i in item:
            count = count+i
        list.append(count)
    return list2

print(fun(list1))
