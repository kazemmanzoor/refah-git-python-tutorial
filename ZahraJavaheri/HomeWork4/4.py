Sentence = input("Enter Sentence:")
words = Sentence.split(" ")
finalstr  = Sentence
reverse = ""

for i in words:
    for j in range(len(i)):
        reverse =  i[j] + reverse
    finalstr = finalstr.replace(i,reverse)
    reverse = ""
print(finalstr)
