def List():
    count=int(input("len of list:"))
    list1=[]
    for i in range(0,count):
        element=input()
        list1.append(element)
    print(list1)
    list1.pop(-1)
    list1.pop(0)
    print(list1)
    
    
    
List()