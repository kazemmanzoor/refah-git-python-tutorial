def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
  
a =int (input ("Enter first number 1: "))    
b =int (input ("Enter second number 2: ")) 
  
result = gcd(a, b)
print("GCD of a & b : ", result) 
