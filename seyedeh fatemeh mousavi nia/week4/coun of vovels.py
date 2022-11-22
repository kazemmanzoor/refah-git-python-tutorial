#count of vovels
def count_vovels():
    str=input("enter the string:")
    counter=0
    for i in range(len(str)):
        if((str[i]=="a" or str[i]=="A") 
        or(str[i]=="e" or str[i]=="E") 
        or(str[i]=="i" or str[i]=="I") 
        or(str[i]=="o" or str[i]=="O") 
        or(str[i]=="u" or str[i]=="U")):
            counter=counter+1
    return counter
 
 
 
print(count_vovels())
        