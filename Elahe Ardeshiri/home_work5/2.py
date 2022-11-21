list1 = [[2,1,8],[7,81,21],[6,4,11]]

def fun(a):
    List = []
    for item in a:
        sortedList = list(reversed(sorted(item)))
        print(sortedList)
        List.append(sortedList)
    return List

print(fun(list1))
