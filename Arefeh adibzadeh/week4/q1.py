func= input()
def isPalindrome(func):
    return func == func[::-1]
ans = isPalindrome(func) 
if ans:
    print("true")
else:
    print("false")
