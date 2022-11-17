numbers = []#1
for i in range(12):
  i += 1
 
  numbers.append(i)
print (numbers)

numbers2 = [n + 2 for n in numbers]#2
print (numbers2)

numbers3 = []#3
for x in numbers2:
    if (x % 2 == 1) :
        x += 1
    numbers3.append(x) 
print (numbers3) 
