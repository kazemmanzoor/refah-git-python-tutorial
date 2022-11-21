num=[]
num2=[]
def jam(num,num2):
    for i in num:
        num.extend(num2)
        print(num)
        return 
num=list(input("please inter your list:"))
num2=list(input("please inter your list:"))
print(jam(num,num2))
        
