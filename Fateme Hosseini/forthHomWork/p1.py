def isPalindrown(n):
    name = ""
    for i in range(len(list(n))):
        name = name+n[len(n)-i-1]
    if(name.upper()!=n.upper()):
        return False
    else:
        return True
