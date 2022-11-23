def pattern_sum(k,n):
    s=0
    t=0
    d=0
    for i in range(1,n+1):
        d=1
        t=0
        for j in range(1,i+1):
            t=t+(k*d)
            d=d*10
        s=s+t
    return s
k=int(input("insert k="))
n=int(input("insert n="))
print(pattern_sum(k,n))
