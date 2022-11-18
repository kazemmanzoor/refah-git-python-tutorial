def fun(x):
    list_keys=tuple(x.keys())
    list_values=tuple(x.values())
    return(list_keys,list_values)

dict1={1:"a",2:"b",3:"c",4:"d"}
print(fun(dict1))
