a=str(input("enter your string:"))
def fun(char , str1):
    strr = str(str1).upper()
    charr = str(char).upper()
    return strr.count(charr)

print(fun(a))
