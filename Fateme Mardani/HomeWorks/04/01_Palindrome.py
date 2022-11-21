word = input("Enter a word:")
reverse = ""
for i in range(len(word)):
    reverse =  word[i] + reverse 
if(reverse == word):
    print("True")
else:
    print("False")
