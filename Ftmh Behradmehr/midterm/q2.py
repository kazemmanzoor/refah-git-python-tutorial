def n_letter_dictionary(str):
    mylist=str.split()
    mydic={}
    for item in mylist:
        print(mydic,len(item))
        mydic[len(item)]=mydic.get(len(item)."")+","+item
    print(mylist)
    
a="I am student in refah university in tehran"
print(n_letter_dictionary(a))

