txt = input("Enter a txt: ")
vowels = ['i', 'o', 'a', 'e', 'u']
count = 0
for char in txt.lower():
    if char in vowels:
        count=count+1
print(count)
  
