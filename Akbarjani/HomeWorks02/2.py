def gcd(x, y): 
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i     
    return gcd

a=int(input("enter number 1:"))
b=int(input("enter number 2:"))

ans=gcd(a,b)
print("answer:",ans)

    
