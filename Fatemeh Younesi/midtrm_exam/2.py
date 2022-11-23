def n_letter_dictionary(a):
    b = a.split(" ")
    c = {}
    for item in b:
        d1 = c.get(len(item) , [])
        if item in d1:
            continue
    return c
