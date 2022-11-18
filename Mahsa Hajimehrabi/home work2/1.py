def func(a,c):
    if c%a==0:
        return "true"
    else:
        return "False"

num1=int(input("put number 1:"))
num2=int(input("put number 2:"))

ans=func(num1,num2)
print("answer:",ans)
