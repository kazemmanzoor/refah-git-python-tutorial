def myFunc(f):
numList = [[34,15,69],[44,55,2],[9,26,88]]
    mylist = []
    for item in f:
        sortedList = list(reversed(sorted(item)))
        mylist.append(sortedList)
    return newlist
print(myFunc(numList))
