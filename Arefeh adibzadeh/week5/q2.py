list=[
    [1,10,6],
    [5,4,12]
    ]
ans=[]
for person in list:
    person.sort()
    person.reverse()
    ans.append(person)
print(ans)
