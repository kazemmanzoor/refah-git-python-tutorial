def p4 (l):
    ar = l.split(" ")
    nr = []
    for i in range(len(ar)):
        nr.append(ar[i][::-1])
    return " ".join( nr)
        

