adad=[
    [1,10,6],
    [5,4,12]
    ]
ans=[]
for person in adad:
    person.sort()
    person.reverse()
    ans.append(person)
print(ans)
