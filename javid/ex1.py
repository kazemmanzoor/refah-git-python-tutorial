def pattern_sum(k,m):
    total=0
    ans=0
    for i in range(1,m+1):
        total=str(k)*i
        print(total)
        ans+=int(total)
    #print(ans)
    return ans
a=int(input ("insert your number"))
b=int(input ("insert ypur number"))
print(pattern_sum(a,b))
        
