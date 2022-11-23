def key_value(dic):
    k = tuple(a.keys())
    v = tuple(a.values())
    return(k, v)

  
strs = input("Enter key values pairs: ")
d = dict(x.split() for x in strs.splitlines())

print("Output:", key_value(d))
