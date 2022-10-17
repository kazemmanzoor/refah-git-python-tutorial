def GCD(d,f):
    r=d%f
    if(r==0):
        return f
    else:
        return GCD(f,r)
n= int(input("Enter the first number1 :"))
m= int(input("Enter the second number2 :"))
print("The GCD of two numbers is:", GCD(n,m))
