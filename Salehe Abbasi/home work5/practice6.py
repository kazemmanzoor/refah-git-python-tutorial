def myFunc(a):
    listKeys = tuple(a.keys())
    listVal = tuple(a.values())
    return (listKeys , listVal)

#--------------------------------
mydic = {1:"a", 2:"b", 3:"c", 4:"d"}
print(myFunc(mydic))
