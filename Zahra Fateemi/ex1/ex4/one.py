s=input(" enter word : ")
s_rev=""
for i in range(len(s)):
   s_rev= s[i]+s_rev
if (s_rev==s):
      print("true")
else:
     print("false")
