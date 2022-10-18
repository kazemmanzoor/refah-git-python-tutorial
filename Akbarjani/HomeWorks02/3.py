def fact(a):
    if (a==0) or (a==1):
        return 1
    else:
        return a*fact(a-1)
    
number=int(input("enter your number:"))
ans=fact(number)

print("answer:",ans)
    
