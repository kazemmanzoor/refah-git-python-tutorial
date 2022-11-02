def myFunc (mylist):
    myarr = mylist.split(" ")
    newarr = []
    for i in range(len(myarr)):
        newarr[i].append( reversed(myarr[i]))
    return " ".join(newarr)
#---------------------------------------------

lists = "you area a good girl ! be sure :)"
print(myFunc(lists))
        
