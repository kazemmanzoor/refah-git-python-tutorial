s = str(input("enter your string:"))

def fun(a):
    dict = {}
    list1 = list(a.upper())
    for item in list1:
        if ["A" , "E" , "O", "I","Y","U"].count(item) >0:
            dict[item] = dict.get(item  , 0)+1
    return dict

print(fun(s))
