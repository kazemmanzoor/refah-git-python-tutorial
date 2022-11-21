def myFunc (mylist):
    myarr = mylist.split(" ")
    newarr = []
    for i in range(len(myarr)):
        newarr.append(myarr[i][::-1])
    return " ".join( newarr)
        
lists = "you are a good girl"
print(myFunc(lists))
