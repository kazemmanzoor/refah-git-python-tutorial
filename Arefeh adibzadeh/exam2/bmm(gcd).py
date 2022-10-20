def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b , a%b)
    
num1 = float(input("please enter first number:"))
num2 = float(input("please enter Second number:"))
print(gcd(num1, num2)) 
