def func(a):
    list1=[]
    for j in a:
        total=0
        for i in j:
            total=total+i
        list1.append(total)
    return list1


input_list=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
ans=func(input_list)
print("output list:",ans)
