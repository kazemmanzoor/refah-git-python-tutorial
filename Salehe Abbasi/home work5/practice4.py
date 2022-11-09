def myFunc(a):
    mydict = {}
    mylist = list(a.upper())
    for item in mylist:
        if ["A" , "E" , "O", "I","Y","U"].count(item) >0:
            mydict[item] = mydict.get(item  , 0)+1
    return mydict




#----------------------------
statement = "you can do what you want . be sure :)"
print(myFunc(statement))
