def none_repeating():
    Len1=int(input("Len of List1:"))
    List1=[]
    Len2=int(input("Len of Lisr2:"))
    List2=[]
    
    
    for i in range(0,Len1):
        el_list1=input("element of List1:")
        List1.append(el_list1)
    print("List1:",List1)
    
    for i in range(0,Len2):
        el_list2=input("element of List2:")
        List2.append(el_list2)
    print("List2:",List2)
    
 
    for i in range(Len1):
        if List2.count(List1[i]) > 0:
            continue
        else:
            List2.append(List1[i])
    return List2
    
    
print(none_repeating())