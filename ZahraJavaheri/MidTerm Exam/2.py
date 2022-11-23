def n_letter_dictionary(str):
    
    str = str.lower()
    WordList = str.split(" ")

    lenlist = []
    FinalDict = {}

    for i in WordList:
        lenlist.append(len(i))
    count = max(lenlist)

    for z in range(count):
        mylist = []
        for Word in WordList:
            if(len(Word) == z+1 and (Word in mylist) == False):
                mylist.append(Word)
        if(len(mylist) != 0):
            FinalDict[z+1] = mylist
    print(FinalDict)
    

string = input("Enter the text:")
n_letter_dictionary(string)
