numList = [[99,10,78],[34,42,23],[52,22,88]]


def myFunc(c):
    my_list = []
    for item in c:
        sortedList = list(reversed(sorted(item)))
        print(sortedList)
        newlist.append(sortedList)
    return my_list

print(myFunc(numList))
        
