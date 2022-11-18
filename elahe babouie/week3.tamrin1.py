def convert(m,n):
    for i in range(len(m)):
        if n.count(m[i]) > 0:
            continue
        else:
            n.append(m[i]) 
    print(n)

list1=input("please insert:")
list2=input("please insert:")

convert(list1,list2)

