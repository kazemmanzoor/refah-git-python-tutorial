def fact(n):
    if (n <=1):
        return 1
    return n * fact(n - 1)

num = float(input("please enter the number:"))
print(fact(num))
