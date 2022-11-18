input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"}

def fun(a):
    list1 = tuple(a.keys())
    list2 = tuple(a.values())
    return (list1 , list2)

print(fun(input_dictionary))
