def isPalindrown(names):
    name2 = ""
    for i in range(len(list(names))):
        name2 = name2+names[len(names)-i-1]
    if(name2==names):
        return True
    else:
        return False
        
#---------------------------------------------------

def myFunc(a):
    counter =0
    for i in range(len(a)):
        if(isPalindrown(a[i])):
            counter = counter+1
    return counter
    
#---------------------------------------------------
    
name=["salehe" , "abbasi" , "asa","shs"]
print(myFunc(name))
