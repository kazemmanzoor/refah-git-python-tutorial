#temp
def reverser(string):
   w = ''
   splited = string.split(' ')
   for i in splited:
     rvs = list(i+' ')
     rvs.reverse()
     for j in rvs:
       w = w + j
   return w
input_string = input('your string:\t')
print(reverser(input_string))
