def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))

print("GCD = ",gcd(m, n))
