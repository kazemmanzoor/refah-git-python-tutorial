def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("Enter number: "))
if number < 0:
    print("er")
else:
    result = factorial(number)
    print("The factorial:", result)