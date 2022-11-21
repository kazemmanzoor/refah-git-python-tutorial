def Func(a):
    b =[]
    i=1
    while i< (len(a)-1):
        b.append(a[i])
        i = i+1
    return b

list1 = [2,4,6,22,44,66]
print(Func(list1))
        
