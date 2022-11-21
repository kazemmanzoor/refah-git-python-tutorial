def func(a):
    k=tuple(a.keys())
    v=tuple(a.values())
    return(k,v)


input_dict ={1:"a", 2:"b", 3:"c", 4:"d"}
ans=func(input_dict)
print("output:",ans)

