def vowels_counter(string):
    vowel = ["a", "e", "i", "o", "y", "u", "A", "E", "I", "O", "Y", "U"]
    list1 = list(string.upper())
    dict1 = {}
    for i in list1:
        if vowel.count(i) > 0:
            dict1[i] = dict1.get(i,0) + 1
    return dict1
    

input_string = input("Please enter your string:")
output = vowels_counter(input_string)
print("Output:", output)
