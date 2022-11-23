name = input("Enter a word:")
r = ""
for i in range(len(name)):
    r =  name[i] + r 
if(r == name):
    print("True")
else:
    print("False")
