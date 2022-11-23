dic = {1:"a", 2:"b", 3:"c", 4:"d"}
#******************************
def Func(x):
    lista = tuple(x.keys())
    listb = tuple(x.values())
    return (lista , listb)


print(Func(dic))
