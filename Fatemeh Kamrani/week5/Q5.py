def dictionary(mydic):
    name = []
    list_keys = list(mydic.keys())
    for i in list_keys:
        A = mydic.get(i)
        count = 0
        for j in A:
            if j>78:
                count = count+1

        if count== len(A):
            name.append(i)
    return name


mydic = {"fatemeh":[1,2 , 4], "ali":[100 , 99 , 98] , "sana":[97 , 98 , 97] , "hasan":[5, 6, 7]}

print(dictionary(mydic))