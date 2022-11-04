input_str = input("enter your string:  ")
input_char =input("enter your character:")
count = 0
for i in input_str :
    if i == input_char :
        count=count+1
        print("===========================")
print ("count of " + input_char + " in " + input_str + "is:   " + str(count))
