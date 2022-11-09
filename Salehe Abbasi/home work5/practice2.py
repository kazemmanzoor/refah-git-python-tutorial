def myFunc(a):
    newlist = []
    for item in a:
        sortedList = list(reversed(sorted(item)))
        print(sortedList)
        newlist.append(sortedList)
    return newlist



#--------------------------------------------------
numList = [[43,1,89],[4,24,2],[90,23,22]]

print(myFunc(numList))
        
