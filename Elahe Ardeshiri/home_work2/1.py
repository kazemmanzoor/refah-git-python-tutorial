a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def multiple(a, b):
    if a % b == 0:
        return "True"
    elif a == 0:
        return "False"
    else:
        return "False"
print(multiple(a, b))
