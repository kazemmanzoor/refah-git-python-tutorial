dic1 = {"zahra":[55,88 , 36], "ali":[99 , 44 , 11] , "sara":[11 , 66 , 74]}



def Func(dic):
    listNameStudent = []
    listKeys = list(dic.keys())
    for item in listKeys:
        grades = dic.get(item)
        count = 0
        for x in grades:
            if x>78:
                count = count+1

        if count== len(grades):
            listNameStudent.append(item)
    return listNameStudent
print(Func(dic1))


