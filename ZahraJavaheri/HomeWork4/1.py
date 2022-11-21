world = input("Enter World:")
reverse = ""
for i in range(len(world)):
    reverse =  world[i] + reverse 
if(reverse == world):
    print("true")
else:
    print("false")
