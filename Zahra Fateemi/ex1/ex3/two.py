def Func(b):
    a = list(b)
    for i in range(len(a)):
        if a[i]%2 != 0:
            a[i]=a[i]+1
        else:
            continue
    return a

list1 = [1,3,5,8]
print(Func(list1))
