def myFunc(a):
    newlist = []
    for item in a:
        sortedList = list(reversed(sorted(item)))
        print(sortedList)
        newlist.append(sortedList)
    return newlist
