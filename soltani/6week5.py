input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"}

def myfunc(func):
    listKeys = tuple(func.keys())
    listVal = tuple(func.values())
    return(listKeys , listVal)
print(myfunc(input_dictionary))
