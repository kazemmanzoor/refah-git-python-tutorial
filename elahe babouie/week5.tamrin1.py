def fun(x):
    list1=[]
    for i in x:
        total=0
        for j in i:
            total=total+j
        list1.append(total)
    return list1

my_list=[[10,11,12,13],
         [14,15,16,17],
         [18,19,20,21]]
print(fun(my_list))
