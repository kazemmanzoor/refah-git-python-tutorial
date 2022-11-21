def func(l1 , l2):
    list1 =l1+l2
    temp = 0
    for i in  range(len(list1)):
        for j in range(len(list1)-1):
            if(list1[j+1]>list1[j]):
                temp=list1[j+1]
                list1[j+1]=list1[j]
                list1[j]=temp
            else:
                continue
    return list1

        
