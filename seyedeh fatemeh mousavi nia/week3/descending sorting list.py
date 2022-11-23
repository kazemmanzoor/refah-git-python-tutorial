#descending sorting list 
def des_sorting_list():
    Len1=int(input("Len of List1:"))
    List1=[]
    Len2=int(input("Len of Lisr2:"))
    List2=[]
    
    
    for i in range(0,Len1):
        el_list1=int(input("element of List1:"))
        List1.append(el_list1)
    print("List1:",List1)
    
    for i in range(0,Len2):
        el_list2=int(input("element of List2:"))
        List2.append(el_list2)
    print("List2:",List2)
  
    list_T =List1+List2
    temp = 0
    for i in  range(len(list_T)):
        for j in range(len(list_T)-1):
            if(list_T[j+1]>list_T[j]):
                temp=list_T[j+1]
                list_T[j+1]=list_T[j]
                list_T[j]=temp
            else:
                continue
    return list_T
    
    
    
print(des_sorting_list())