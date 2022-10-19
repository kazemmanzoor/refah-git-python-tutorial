def multiple (m, n):
    if n == 0:
        return "False"
    elif m % n == 0:
        return "True"
    else:
        return "False"

m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))

print(multiple(m, n))
