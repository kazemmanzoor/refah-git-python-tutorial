a=input("enter word=")
a_rev=""
for i in range(len(a)):
    a_rev=a[i]+a_rev
if(a_rev==a):
    print("true")
else:
    print("false")
