def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
num1 = float(input("enter number1:"))
num2 = float(input(" enter number2:"))
print(gcd(num1, num2)) 
