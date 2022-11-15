score = {
    "zahra" : [78, 94, 88],
    "sara" : [66, 54, 100],
    "maryam" : [65, 67, 45],
    "mina" : [89, 93, 82],
    "saba" : [79, 83, 80]
}
count = 0

for i in score:
    for j in score[i]:
        if(j >= 78):
            count = count + 1
    if(count == 3):
        print(i)
    count = 0


