def func(a):
    b = list(a)
    for i in range(len(b)):
        if b[i]%2 != 0:
            b[i]=b[i]+1
        else:
            continue
    return b

x= [1, 2, 3, 4]
print(func(x));