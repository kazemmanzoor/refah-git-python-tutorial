def factorial(m):
   if m == 1:
       return m
   else:
       return m*factorial(m-1)

n = int(input("enter a number: "))

if n < 0:
   print("baraye adad manfi factorial mojod nist")
elif n == 0:
   print(n, "! = ", 1)
else:
   print(n ,"! = ", factorial(n))
