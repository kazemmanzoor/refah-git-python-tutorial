import InputListModule as Rec

MyList = []
Rec.input5(MyList)

for i in range(len(MyList)):
    if ( (MyList[i] % 2) != 0):
        MyList[i] = MyList[i] + 1
print(f"FinalList: {MyList}")
