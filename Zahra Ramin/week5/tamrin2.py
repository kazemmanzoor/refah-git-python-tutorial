def func(a):
    newlist = []
    for item in a:
        sortedList = list(reversed(sorted(item)))
        newlist.append(sortedList)
    return newlist




nList = [[26,5,25],[12,13,2],[21,78,66]]

print(func(nList))
  
