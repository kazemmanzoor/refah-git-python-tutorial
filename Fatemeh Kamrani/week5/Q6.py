def Ftuple(a):
    A=tuple(a.keys())
    B=tuple(a.values())
    return(A,B)

mydic ={1:"a", 2:"b", 3:"c", 4:"d"}
print(Ftuple(mydic))