a=[[2,3,4],
   [3,4,5]]
b=[[4,-3,12],
   [1,1,5],
   [1,3,2]]
c=[]
for person in a and b:
    for i in range(0,(len(a) and len(b))):
        c=(a[i])*(b[i])
        c=c+c
print(c)
