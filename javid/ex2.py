m=str(input("insert your sentence"))
def n_letter_dictionary(a):
    dic={}
    m2=m.lower()
    m2=m.split(" ")
    for item in m2:
        m2= dic.get(len(item),[])
        if item in m2:
            continue
        else:
            m3=dic.get(len(item),[])
            m3.append(item)
            dic[len(item)]=m3
    return dic
print(n_letter_dictionary(m))

   
    
