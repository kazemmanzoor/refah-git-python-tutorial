def n_letter_dictionary(str1):
    list1 = str1.split(" ")
    dic1 = {}
    dic2 = {}
    for item in list1:
        val3 = dic1.get(len(item) , "").split(" ")
        if item in val3:
            continue
        else:
            dic1[len(item)] =dic1.get(len(item) , "") + " "+ item
    for item in list1:
        val2 = dic1.get(len(item) ).split(" ")
        dic2[len(item)] = val2[1::]
    return dic2


#------------------------------
val1 = "i am am student in refah"
print(n_letter_dictionary(val1))
