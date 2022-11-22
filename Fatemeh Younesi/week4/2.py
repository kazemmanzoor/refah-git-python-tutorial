def myFunc(mytxt):
    txt = mytxt.upper()
    counter = 0
    counter = txt.count("A")+txt.count("E")+txt.count("O")+txt.count("I")+txt.count("U")
    return counter
