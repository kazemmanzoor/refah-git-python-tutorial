word = input("Enter Word:")
reverse = ""
for i in range(len(word)):
    reverse =  word[i] + reverse 
if(reverse == word):
    print("true")
else:
    print("false")
