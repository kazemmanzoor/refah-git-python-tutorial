def gcd(a,b):
    if (a>b):
       small=b
    else:
        small=a
    for i in range(1,small+1):
        if (a%i==0 and b%i==0):
            gcd=i
    return gcd
a=int(input("insert num a="))
b=int(input("insert num b="))
print(gcd(a,b))
