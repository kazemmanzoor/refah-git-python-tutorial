def n_letter_dictionary(my_string):
    my_string = my_string.lower().split()

    L= []
    for key in my_string:
        if len(key) >1:
            l={len(key):[key]}
            L.append(l)
    L.sort()         
    return L
s="The way you see people is the way you treat them and the Way you treat them is what they become"
print(n_letter_dictionary(s))
