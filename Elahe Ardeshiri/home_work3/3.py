list1 = [1,2,3,4,5]
list2=[6,7,8,9,4=10]

def myFunc(a , b):
    list =a+b
    temp = 0
    for i in  range(len(list)):
        for j in range(len(list)-1):
            if(list[j+1]>list[j]):
                temp=list[j+1]
                list[j+1]=list[j]
                list[j]=temp
            else:
                continue
    return list

print(myFunc(list1 , list2))
