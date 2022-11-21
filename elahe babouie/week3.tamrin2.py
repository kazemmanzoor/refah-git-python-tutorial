def func(list1):
    list2=list(list1)
    for i in range(len(list2)):
        if list2[i]%2 !=0:
            list2[i]=list2[i]+1
        else:
             continue
            
    return list2
            
list3=[1,2,3]
print(func(list3))
