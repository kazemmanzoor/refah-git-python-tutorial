#count of each sound
def count_sounds():
    count_a=0
    count_e=0
    count_i=0
    count_o=0
    count_u=0
    string=input("String:")
    for each in range(len(string)):
        if string[each]==" ":
            each=each+1
        else:
            if(string[each]=="a" or string[each]=="A"):
                count_a=count_a+1
            elif(string[each]=="e" or string[each]=="E"):
                count_e=count_e+1
            elif(string[each]=="i" or string[each]=="I"):
                count_i=count_i+1
            elif(string[each]=="o" or string[each]=="O"):
                count_o=count_o+1
            elif(string[each]=="u" or string[each]=="U"):
                count_u=count_u+1
            else:
                continue
        dic={
       "a":count_a,    
       "e":count_e,
       "i":count_i,
       "o":count_o,
       "u":count_u
       }
    return  dic
    
    
    
    
print(count_sounds())