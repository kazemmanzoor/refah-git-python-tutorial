def isPal(n):
    n2 = ""
    for i in range(len(list(n))):
        n2 = n[i]+n2
    if(n2==n):
        return True
    else:
        return False
        

def mypractice(list1):
    counter =0
    for i in range(len(list1)):
        if(isPal(list1[i])):
            counter = counter+1
    return counter
    



    
name=["fateme" , "sds" , "hoseiny"]
print(mypractice(name))
