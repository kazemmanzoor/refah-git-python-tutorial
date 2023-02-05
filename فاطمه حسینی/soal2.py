def n_letter_dictionary(fh1):
    e1 = fh1.split(" ")
    print(e1) 
    dict1 = {}
    for item in e1:
        dict1[len(item)] =dict1.get(len(item) , " ")+" "+ item
        
    return dict1


val1 = "holle iam student in refah university "
print(n_letter_dictionary(val1))
