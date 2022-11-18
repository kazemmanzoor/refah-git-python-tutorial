def fun(vowels):
    vowel = vowels.upper()
    counter = 0
    counter = vowel.count("A")+vowel.count("E")+vowel.count("O")+vowel.count("I")+vowel.count("U")
    return counter

print(fun("ok everythings"))
