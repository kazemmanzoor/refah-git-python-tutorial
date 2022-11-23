def funclist(list1 , list2):
    for i in range(len(list1)):
        if list2.count(list1[i]) > 0:
            continue
        else:
            list2.append(list1[i])
    print(list2)


list1=input("list1:")
list2=input("list2:")
funclist(list1 , list2)