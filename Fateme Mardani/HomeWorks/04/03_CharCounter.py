inputString = input("Enter a string:")
character = input("Enter the character you want to count:")

count = 0

for i in inputString:
	if i == character:
		count = count + 1

print (str(count))
