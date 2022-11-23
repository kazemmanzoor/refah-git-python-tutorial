def pattern_sum(a,b):
    strnum=a
    count=int(a)
    
    for i in range (b-1):
       #num=str(val[0]*item)
        a=a+strnum
        count=count+int(a)
    return(count)
    
num1=input("enter number :")
num2=int(input("enter teadad :"))
print(pattern_sum(num1,num2))
