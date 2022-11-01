def func(a):
    b=[]
    i=1
    while i<(len(a)-1):
        b.append(a[i])
        i=i+1
    return b


list1=[int(x) for x in input("Enter your List:").split()]

ans=func(list1)
print("output list:",ans)
