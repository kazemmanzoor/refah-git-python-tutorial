def n_letter_dirctory(str):
    
    str=str.lower()
    wordlist= str.split("")
    
    mydict={}
    lenlist=[]
    for i in wordlist:
        lenlist.append(len(i))
    count = max(lenlist)
    for j in range(count):
        mylist1=[]
        for word in wordlist:
             if(len(word)== j+1 and (word in mylist1)== False):
                 mylist1.append(word)
        if(len(mylist1)!=0 ):
            mydict[j+1]= mylist1
    print(mydict)


string=input("enter txt :")
print(n_letter_dirctory(string))

#ارور داشت
