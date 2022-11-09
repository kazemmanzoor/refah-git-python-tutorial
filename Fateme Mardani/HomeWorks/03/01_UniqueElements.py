def convert(m,n):
    for i in range(len(m)):
        if n.count(m[i]) > 0:
            continue
        else:
            n.append(m[i]) 
    print(n)

list1=input("Please enter the first list:")
list2=input("Please enter the second list:")

convert(list1,list2)
