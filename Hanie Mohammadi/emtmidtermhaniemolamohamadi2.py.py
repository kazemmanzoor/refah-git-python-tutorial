def n_letter_dictionary(str):
    str =str.lower()
    listsword = str.split(" ")
    
    listslen={}
    dict1={}

    for n in listsword:
        listslen.append(len(n))
    count = max(listsword)

    for m in range(count):
        mylists = []
        for w in listsword:

            if(len(w) == m+1 and (w in mylists) == False):
                mylists.append(w)
        if(len(mylists) !=0):
            dict1[m+1] = mylists
    print(dic1)

        
    

string = " lotfan matn ra vared konid:"
n_letter_dictionary(string)

    
        
        
        
    


     



    
    #haniemolamohammadi soal 2


