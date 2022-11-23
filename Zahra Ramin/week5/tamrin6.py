def func(a):
    listKeys = tuple(a.keys())
    listVal = tuple(a.values())
    return (listKeys , listVal)


fdic = {1:"a", 2:"b", 3:"c", 4:"d"}
print(func(fdic))
