def factoriel(a):
    if a==0:
        return 1
    else:
        return a*factoriel(a-1)
print(factoriel(3))
