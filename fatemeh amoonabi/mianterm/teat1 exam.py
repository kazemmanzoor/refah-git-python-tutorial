def pattern_sum(k,m):
    total=0
    ans=0
    for i in range(1,m+1):
        total=str(k)*i
        print(total)
        ans+=int(total)
    print(ans)
a=int(input("insert number "))
b=int(input("insert number "))
print(pattern_sum(a,b))



























    
