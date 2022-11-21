def func(m):
    n=[]
    i=1
    while i< (len(m)-1):
        n.append(m[i])
        i=i+1
    return n

l1=[1,2,5,8,4,89,4,90,45]
print(func(l1))
