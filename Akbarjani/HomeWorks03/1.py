def convert(a,b):
    for i in range(len(a)):
        if (b.count(a[i])) > 0:
            continue
        else:
            b.append(a[i])
    print(b)

list1=[int(x) for x in input("Enter List1:").split()]
list2=[int(y) for y in input("Enter List2:").split()]
convert(list1,list2)
