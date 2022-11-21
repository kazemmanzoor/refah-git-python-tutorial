def fun(x):
    my_dict={}
    listvowel=["a","A","e","E","o","O","u","U","i","I"]
    list1=list(x.upper())
    for i in list1:
        if listvowel.count(i)>0:
            my_dict[i]=my_dict.get(i,0)+1
    return my_dict

y="salam khobi chetori"
print(fun(y))
