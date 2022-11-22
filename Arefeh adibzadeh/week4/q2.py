def myFunc(word):
    txt = word.upper()
    counter = 0
    counter = txt.count("A")+txt.count("E")+txt.count("O")+txt.count("I")+txt.count("U")
    return counter
print(myFunc())
