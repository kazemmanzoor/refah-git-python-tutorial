val1=["hello","ali"]
val2=["how","are" , "you"]

def convert(a , b):
    for i in range(len(a)):
        if b.count(a[i]) > 0:
            continue
        else:
            b.append(a[i])
    print(b)

convert(val1 , val2)
