age = {
    "zahra" : 22,
    "sara" : 20,
    "maryam" : 15,
    "mina" : 25,
    "saba" : 32
}
NameList = []
ValueList = []
FinalList = []

for i in age:
    NameList.append(i)
    ValueList.append(age[i])

Tname = tuple(NameList)
Tvalue = tuple(ValueList)
FinalList.append(Tname)
FinalList.append(Tvalue)

print(tuple(FinalList))


