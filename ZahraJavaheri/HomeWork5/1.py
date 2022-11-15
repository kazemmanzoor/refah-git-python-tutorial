MyList = [
    [1,2,3,4],
    [4,5,6,7],
    [8,9,10,11]
]

SubList = []
sub = 0
for i in MyList:
    for j in i:
        sub = sub + j
    SubList.append(sub)
    sub = 0
print(f"SubList is: {SubList}")
