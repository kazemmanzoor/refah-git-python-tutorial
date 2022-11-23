question 1:
a=[1,3,5,7]
b=[10,5,3,4,12]
for i in range(len(a)):
    if(b.count(a[i]))>0:
        continue
    else:
        b.append(a[i])
print(b)

/////

question 4:
a:[1,-3,2,-4,-9]
a.remove (1,9)
a
[-3,2,-4]

/////

question 2:
a=[12,3,4,5,6]
for i in range(len(a)):
    if (a[i]%2==1):
        a[i]=a[i]+1
print(a)


