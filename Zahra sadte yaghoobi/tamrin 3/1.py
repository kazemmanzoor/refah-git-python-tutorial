def difference (list1, list2):
   list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
   return list_dif
   x=[]
   y =[]
x=str(input("enter1: " ))
y=str(input("enter2:  " ))


z = difference (x, y)

print("Difference of first and second String: " + str(z))
print("--------------------------------------")


if not z:
    print(">>>First and Second list are Equal<<<")
   
else:
    print(">>>First and Second list are Not Equal<<<")
