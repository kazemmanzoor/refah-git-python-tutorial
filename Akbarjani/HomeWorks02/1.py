def func(a,b):
    if b%a==0:
        return "true"
    else:
        return "False"

num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))

ans=func(num1,num2)
print("answer:",ans)
