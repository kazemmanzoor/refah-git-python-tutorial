def myFunc(a):
    b =[]
    i=1
    while i< (len(a)-1):
        b.append(a[i])
        i = i+1
    return b

#--------------------------------------


mylist = [1,5,3,75,2 ,4,2,13]
print(myFunc(mylist))
        
