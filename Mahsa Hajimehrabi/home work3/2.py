def myFunc(list2):
    list1 = list(list2)
    for i in range(len(list1)):
        if list1[i]%2 != 0:
            list1[i]=list1[i]+1
        else:
            continue
    return list1
