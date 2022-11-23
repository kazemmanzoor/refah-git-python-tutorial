def n_letter_dictionary(mylist):
    dict={}
    count={}
    l1={}
    value={}
    mylist=mylist.lower()
    new_list=mylist.split(" ")
    for item in new_list:
        count=l1.get(len(item) , [])
        #print(count)
        if item in count:
            continue
        else:
            value=l1.get(len(item) , [])
            value.append(item)
            l1[len(item)]=value
    return l1
    #print(l1)
mylist=input("write your sentence:")
print(n_letter_dictionary(mylist))
