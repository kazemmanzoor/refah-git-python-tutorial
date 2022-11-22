def fact(num):
    if num>=0:
        if num==1 or num==0:
            return 1
        else:
            return num*fact(num-1)
    else:
        return "invalid number"
        
num=int(input("number:"))        
print(fact(num))