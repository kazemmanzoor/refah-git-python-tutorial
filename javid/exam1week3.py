from collections import Counter
a=[]
b=[]
c=[]
def nim(a,b):
    c=list((Counter(a)-Counter(b)).elements())
    b.extend(c)
    return b
a=list(input("please inter your list: "))
b=list(input("please inter your list: "))
print(nim(a,b))

            
            
            
            
            
