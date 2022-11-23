def polindrome(str):
    n=len(str)-1
    for i in range(len(str)):
        if (str[i]==str[n-i]):
            return  True
        else:
            return False
  
str1=input("str1:")
print(polindrome(str1))