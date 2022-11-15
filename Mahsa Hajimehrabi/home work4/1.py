def isPalindrown(names):
    name2 = ""
    for i in range(len(list(names))):
        name2 = name2+names[len(names)-i-1]
    if(name2.upper()==names.upper()):
        return True
    else:
        return False
