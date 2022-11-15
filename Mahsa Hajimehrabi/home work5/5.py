def myFunc(mydic):
    listName = []
    listKeys = list(mydic.keys())
    for item in listKeys:
        grades = mydic.get(item)
        count = 0
        for i in grades:
            if i>78:
                count = count+1

        if count== len(grades):
            listName.append(item)
    return listName
