def fun(my_string):
    x=my_string.split()
    y=[]
    for i in range(len(x)): y.append(x[i][::-1])
    
    return "".join(y)
    
a=input("enter string=")
print(fun(a))
