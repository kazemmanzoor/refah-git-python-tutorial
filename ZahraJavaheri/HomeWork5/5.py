score = {
    "zahra" : [78, 94, 88],
    "sara" : [66, 54, 100],
    "maryam" : [65, 67, 45],
    "mina" : [89, 93, 82],
    "saba" : [79, 83, 80]
}
count = 0
NameList = []

for i in score:
    for j in score[i]:
        if(j >= 78):
            count = count + 1
    if(count == 3):
        NameList.append(i)
    count = 0

print(NameList)
