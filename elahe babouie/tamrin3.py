def factorial(a):
    if (a==0 or a==1):
        return 1
    else:
        return a*factorial(a-1)   
a=int(input("number=")) 
print(factorial(a))       