def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact

n = int(input('enter the number: '))
result = factorial(n)
print('the answer is: ' f'{result}')