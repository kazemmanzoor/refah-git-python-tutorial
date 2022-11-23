def pattern_sum(x,y):
    sum=0
    ans=0
    for i in range(1,y+1):
        sum=str (x)*i
        print(sum)
        ans+=int(sum)
        print (ans)
a=int(input("insert number"))
b=int(input("insert number"))
print(pattern_sum(a,b))
        
