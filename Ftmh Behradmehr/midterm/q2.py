def n_letter_dictionary(my_str):
    mylist=my_str.split()
    #print(mylist)
    mydic={}
    for item in mylist:
        print(mydic,len(item))
    #    mydic[len(item)]=mydic.get(len(item)."")+","+item
    print(mylist)
    
a="I am student in refah university in tehran"
print(n_letter_dictionary(a))

