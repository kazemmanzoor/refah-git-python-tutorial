def myFunc(a):
    b = a[1:len(a)-1:]
    return b

mylist = list(input('your list: ').split('.'))
print(myFunc(mylist))
