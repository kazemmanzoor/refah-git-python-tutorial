def sortlist(a , b):
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

list = [1, 2, 3, 4, 5]
list2=[10, 20, 18, 100]
print(sortlist(list , list2))
        