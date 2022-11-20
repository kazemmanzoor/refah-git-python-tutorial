listeman = [[2,10,3],[8,2,4],[1,9,5]]
def myfunc(func):
    mylist = []
    for item in func:
       sortedlist = list(reversed(sorted(item)))
       mylist.append(sortedlist)
    return mylist
print(myfunc(listeman))
