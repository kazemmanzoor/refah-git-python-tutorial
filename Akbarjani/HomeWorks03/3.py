def func(a,b):
    f_list = a+b
    c = 0
    for i in  range(len(f_list)):
        for j in range(len(f_list)-1):
            if((f_list[j+1])>(f_list[j])):
                c=f_list[j+1]
                f_list[j+1]=f_list[j]
                f_list[j]=c
            else:
                continue
    return f_list


list1=[int(x) for x in input("Enter List1:").split()]
list2=[int(y) for y in input("Enter List2:").split()]

ans=func(list1,list2)
print("output list:",ans)
