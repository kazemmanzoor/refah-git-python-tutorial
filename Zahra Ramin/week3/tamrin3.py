def sorted_lists(list1 , list2):
    list3 = []
    for i in list1:
        if int(i) not in list3:
            list3.append(int(i))
    for j in list2:
        if int(j) not in list3:
            list3.append(int(j))
    return sorted(list3,reverse=True)
list1 = list(input('\nlist 1: ').split('.'))
list2 = list(input('\nlist 2: ').split('.'))
print(sorted_lists(list1, list2))
