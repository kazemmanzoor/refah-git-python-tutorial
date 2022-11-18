a=[10,11,3,5,7]
b=[10,5,3,4,12,3]
for i in range(len(a)):
    if(b.count(a[i]))>0:
        continue
    else:
        b.append(a[i])

print(b)
