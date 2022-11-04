s = input("Enter :")
def isPalindrome(s):
 return s == s[::-1]
ans = isPalindrome(s) 
if ans:
 print("<<true>>>")
else:
 print("<<false>>")
