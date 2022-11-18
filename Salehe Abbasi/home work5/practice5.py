def myFunc(mydic):
    listNameStudent = []
    listKeys = list(mydic.keys())
    for item in listKeys:
        grades = mydic.get(item)
        count = 0
        for i in grades:
            if i>78:
                count = count+1

        if count== len(grades):
            listNameStudent.append(item)
    return listNameStudent


#------------------------------
dic1 = {"salehe":[35,90 , 53], "fateme":[98 , 24 , 87] , "sakine":[94 , 100 , 79]}
print(myFunc(dic1))
