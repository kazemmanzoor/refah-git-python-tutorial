def func(a):
    list1=[]
    for item in a:
        list_s=list(reversed(sorted(item)))
        print(list_s)#1
        list1.append(list_s)#2
    return list1


input_list=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
ans=func(input_list)
print("output list:",ans)
