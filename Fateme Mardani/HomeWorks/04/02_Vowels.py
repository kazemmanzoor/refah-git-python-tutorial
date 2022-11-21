def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels
  
inputString = str(input("Please type a sentence: "))

print(countvowels(inputString))
