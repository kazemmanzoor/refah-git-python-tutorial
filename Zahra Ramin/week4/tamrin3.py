def myFunc(char , str1):
    count=0
    mystr = str(str1).upper()
    mychar = str(char).upper()
    return mystr.count(mychar)

mystr =input("please type str: ")
mystr =input("please type char: ")

print(myFunc( mystr,mystr))
