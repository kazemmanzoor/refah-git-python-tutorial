def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
        

num_1=int(input("num_1:"))
num_2=int(input("num_2:"))
print(gcd(num_1,num_2))