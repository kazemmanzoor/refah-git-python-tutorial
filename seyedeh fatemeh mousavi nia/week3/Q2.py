def num_list():
    Len=int(input("Len of List:"))
    List=[]
    for i in range(0,Len):
        element=int(input("element:"))
        if element>=0:
            List.append(element)
        else:
            print("value can not be negative.")
    print(List)
    
    
    
    for i in range(Len):
        if List[i]%2!=0:
            List[i]=List[i]+1
        else:
            continue
            
    return List
        
print(num_list())