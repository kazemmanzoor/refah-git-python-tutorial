def func(dict1):
    person=[]
    Keys1=list(dict1.keys())
    for j in Keys1:
        total=0
        score=dict1.get(j)
        for i in score:
            if i>=78:
                total=total+1
        if total==len(score):
            person.append(j)
    return person


input_dict = {"mohadese":[100,90,80],"fateme":[79,89,78],"zahra":[40,30,20]}
ans=func(input_dict)
print("output dict:",ans)
