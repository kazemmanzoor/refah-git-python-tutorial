mylist=[1,2,3,4,5,6,7]
def myfunc(a):
    b=list(a)
    for i in range(len(b)):
         if b[i]%2 !=0:
             b[i]=b[i]+1
         else:
                continue
    return b
print(myfunc(mylist))
