scores=[
    [12,13,14],
    [15,16,17],
    [18,19,20]
    ]
sum=[]
for person in scores:
    total=0
    for i in range(0,len(person)):
        total=total+person[i]
    sum.append(total)
    print(sum)
