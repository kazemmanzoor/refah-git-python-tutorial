def pattern_sum(k,m):
    final=0
    ans=0
    for i in range(1,m+1):
        final=str(k)*i
        print(final)
        ans+=int(final)
    return ans
number1=int(input("inser a number"))
number2=int(input("inser a number"))        
print(pattern_sum(number1,number2))
