vowels = 'aeiou'

ip_str = input(" please Enter something: ")


ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:

   if char in count:

       count[char] += 1
       print('======================================')
print(count)
