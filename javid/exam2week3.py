def fard(a):
    b=list(a)
    for i in range(len(b)):
        if b[i]%2 !=0:
           b[i]=b[i]+1
        else:
            continue
    return b

a=list(input("please inter your num:"))
print(fard(a))


       
