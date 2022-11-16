def myFunc(a):
    newlist = []
    for item in a:
        sortedList = list(reversed(sorted(item)))
        print(sortedList)
        newlist.append(sortedList)
    return newlist

numList = [[40,10,28],[4,24,2],[9,23,9]]

print(myFunc(numList))
