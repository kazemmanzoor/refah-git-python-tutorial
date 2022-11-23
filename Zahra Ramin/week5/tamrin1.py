def func(a):
    listSum = []
    for item in a:
        count = 0
        for i in item:
            count = count+i
        listSum.append(count)
    return listSum




list1 = [ int(a) for a in input("Enter your list: ").split() ]
print(func(list1))
