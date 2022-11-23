a=input("num1:")
b=input("num2:")
def ref(a,b):
    str_b=str(b)
    jam=b
    jam_str=str(b)
    for i in range(1,a):
jam_str=jam_str+str_b
jam=jam+int(jam_str)
return jam
temp=ref(a,b)
print("----------")
print(temp)
