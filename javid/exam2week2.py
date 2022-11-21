def gcd(x,y):
    gcd=1
    if x%y==0:
        return y
    for k in range(int(y/2),0,-1):
        if x%k==0 and y%k==0:
            gcd=k
            break
    return gcd



num1 =int( input("please enter a  first number:"))
num2 = int(input("please enter a second number:"))
print("your gcd is : ",gcd(num1 , num2))
