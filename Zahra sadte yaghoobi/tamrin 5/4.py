
y= str(input("Enter  something:"))
a = 0
e = 0
i = 0
o = 0
u = 0
for n in y:
    if(n == "a" or n == "A"):
        a= a+1
    elif(n == "e" or n == "E"):
        e= e+1
    elif(n == "i" or n == "I"):
        i= i+1
    elif(n== "o" or n == "O"):
        o= o+1
    elif(n == "u" or n == "U"):
        u= u+1
m = dict({"a":a ,"e": e, "i": i, "o": o, "u": u}) 
print("--------------------------------")
print(" result = ",m)
