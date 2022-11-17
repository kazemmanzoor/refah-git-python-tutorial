dic1 = {"ali":[20,18.25 , 14], "sara":[14 , 15 , 20] , "saeed":[18 , 20 , 17]}

def fun(a):
    list2 = []
    list3 = list(a.keys())
    for item in list3:
        grades = a.get(item)
        count = 0
        for i in grades:
            if i>78:
                count = count+1

        if count== len(grades):
            list2.append(item)
    return list2

print(fun(dic1))
