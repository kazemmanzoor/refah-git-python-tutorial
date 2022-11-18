def fun(x):
    my_list=[]
    for i in x:
        list_sorted=list(reversed(sorted(i)))
        print(list_sorted)
        my_list.append(list_sorted)
        
    return my_list

a=[[12,13,14],
   [15,19,17],
   [18,20,11]]
print(fun(a))
