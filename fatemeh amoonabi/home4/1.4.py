world= input()
def isPalindrome(world):
    return world == world[::-1]
ans = isPalindrome(world) 
if ans:
    print("true")
else:
    print("false")
