def myFunc(a , b):
    list1 =a+b
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

#------------------------------

list = [1,4,2,8,5]
list2=[6,3,14,9,4]
print(myFunc(list , list2))
        
