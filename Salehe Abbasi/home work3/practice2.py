def myFunc(b):
    a = list(b)
    for i in range(len(a)):
        if a[i]%2 != 0:
            a[i]=a[i]+1
        else:
            continue
    return a


#--------------------------------------

mylist = [1,3,4,5,6]
print(myFunc(mylist));
