def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("number1="))  
b=int(input("number2=")) 
print(gcd(a,b))        