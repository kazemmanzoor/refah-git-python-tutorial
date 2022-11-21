import InputListModule as Rec

list1 = []
list2 = []
Rec.input5(list1)
Rec.input5(list2)

list1.extend(list2)
print(list1)

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
           list1[i], list1[j] = list1[j], list1[i]
print (list1)


