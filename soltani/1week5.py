listeman = [[2,10,3],[8,2,4],[1,9,5]]

def myfunc(func):
    mylist = []
    for item in func:
        count = 0
        for i in item:
            count=count + i
            mylist.append(count)
    return mylist
print(myfunc(listeman))

