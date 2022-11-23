def myFunc (mylist):
    myarr = mylist.split(" ")
    a= []
    for i in range(len(myarr)):
        a.append(myarr[i][::-1])
    return " ".join( a)
        
input_string = "this is a sample test"
print(myFunc(input_string ))
