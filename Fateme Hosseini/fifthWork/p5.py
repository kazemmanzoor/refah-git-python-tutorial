def par(dic):
    Students = []
    Keys = list(dic.keys())
    for item in Keys:
        g = dic.get(item)
        c = 0
        for i in g:
            if i>78:
                c = c+1

        if count== len(g):
            Students.append(item)
    return Students



