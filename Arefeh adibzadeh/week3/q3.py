def myfunc(a):
  newlist = []
  for item in a :
    sortedlist = list(reversed(sorted(item)))
    newlist.append(sortedlist)
  return newlist
l1=input("enter your list")
l2=l1.split("*")
print(l2)
l3=[]
for item in range(len(l2)):
  l3.append(l2[item].split(","))
print(l3)
