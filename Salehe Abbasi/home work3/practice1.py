def convert(a , b):
    for i in range(len(a)):
        if b.count(a[i]) > 0:
            continue
        else:
            b.append(a[i])
    print(b)

#----------------------------------------
    
name1=["salehe","abbasi"]
name2=["fateme","hosseini" , "salehe"]
convert(name1 , name2)
