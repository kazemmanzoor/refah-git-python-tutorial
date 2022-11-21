sedaha='aeiou'
star=input("please insert your string:")
n = {}.fromkeys(sedaha,0)
for char in star:
    if char in n:
        n[char] += 1
print(n) 
    
#def vared():
   #star=input("please insert your string:") 
