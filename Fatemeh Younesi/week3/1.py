def convert(a,b):
    for i in range(len(a)):
        if b.count(a[i])>0:
            continue
        else:
            b.append(a[i])
a=input("add list a=")
b=input("add list b=")
print(b)
