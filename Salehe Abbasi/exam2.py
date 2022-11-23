def n_letter_dictionary(str1):
    list1 = str1.split(" ")
    dic1 = {}
    for item in list1:
        val3 = dic1.get(len(item) , [])
        if item in val3:
            continue
        else:
            val4 = dic1.get(len(item) , [])
            val4.append( item)
            dic1[len(item)] = val4
  
    return dic1


#------------------------------
val1 = "i am am student in refah"
print(n_letter_dictionary(val1))
