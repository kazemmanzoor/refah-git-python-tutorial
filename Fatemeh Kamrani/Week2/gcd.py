def gcd (a,b):
	if a>b:
		bmm=b
	elif a<b:
		bmm=a
	while bmm>1:
		if a%bmm==0 and b%bmm==0:
			print("bmm=", bmm)
			break
		else:
			bmm -=1
			if a%bmm==0 and b%bmm==0:
			 	return print("bmm= " , bmm)
			 	
num1=int(input("num1= "))
num2=int(input("num2= "))
print(gcd(num1,num2))