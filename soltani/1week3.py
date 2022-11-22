def myfunc(a, b):
    for i in range(len(a)):
        if b.count(a[i])>0:
            continue
        else:
            b.append(a[i])
    print(b)
name0=["dina","sara","baran"]
name1=["fatemeh","sara","mona"]
myfunc(name0,name1)
