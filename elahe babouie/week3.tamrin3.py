def func(a,b):
    f_list =a+b
    c=0
    for i in range(len(f_list)):
        for j in range(len(f_list)-1):
            if((f_list[j+1])>(f_list[j])):
                c=f_list[j+1]
                f_list[j+1]=f_list[j]
                f_list[j]=c
            else:
                  continue
    return f_list


list1=[1,42,5,8,9]
list2=[0,3,6,8,10]
print(func(list1,list2))

    
