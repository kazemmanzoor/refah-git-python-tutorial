p = input("Enter string:")
a = 0
e = 0
i = 0
o = 0
u = 0
for j in p:
    if(j == "a" or j == "A"):
        a= a+1
    elif(j == "e" or j == "E"):
        e= e+1
    elif(j == "i" or j == "I"):
        i= i+1
    elif(j == "o" or j == "O"):
        o= o+1
    elif(j == "u" or j == "U"):
        u= u+1
dictionary = dict({"a":a ,"e": e, "i": i, "o": o, "u": u}) 
print(dictionary)
