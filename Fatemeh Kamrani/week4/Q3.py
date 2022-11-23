def countchar(char , str1):
    instr = str(str1).upper()
    inchar = str(char).upper()
    return instr.count(inchar)

print(countchar("a" , "salaaaaam"))