def func(a):
    vowel=["a","A","e","E","i","I","o","O","u","U"]
    list1=list(a.upper())
    dict1={}
    for i in list1:
        if vowel.count(i)>0:
            dict1[i]=dict1.get(i,0)+1
    return dict1
    

input_string = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit, molestias!"
ans=func(input_string)
print("output string:",ans)

