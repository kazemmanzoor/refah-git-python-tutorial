def n_letter_dictionary(word):
    l1=word.split(" ")
    ans={}
    for item in l1:
        print(item,len(item))
        ans[len(item)]=ans.get(len(item),"")+ ","+item
    print(ans)
sr="i am in student in refah university"
print(n_letter_dictionary(sr))
