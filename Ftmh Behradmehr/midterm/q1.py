def pattern_sum(k,m):
    total=0
    jam=0
    for i in range (1,m+1):
       total=str(k)*i
       print(total)
       
       jam=int(total)+jam
    print(jam)

x=int(input("please inter your num1"))
y=int(input("please inter your num2"))
print(pattern_sum(x,y))
