def pattern_sum (k,m):
    total=0
    answer=0
    for i in range(1,m+1):
        total=str(k)*i
        print(total)
        answer+=int(total)
    return answer
num1=int(input("please enter the first number:"))
num2=int(input("please enter the rep number:"))
print("your new num is:",(pattern_sum(num1,num2)))
