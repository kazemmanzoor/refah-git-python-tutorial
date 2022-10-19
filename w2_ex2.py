def gcd(a, b):

	if a > b:
		less = b
	else:
		less = a
	for i in range(1, less + 1):
		if((a % i == 0) and (b % i == 0)):
			gcd = i
			
	return gcd

n_1 = int(input('enter 1st number: '))
n_2= int(input('\nenter 2nd number: '))
result = gcd(n_1, n_2)

print('The GCD of ' f'{n_1} ' 'and ' f'{n_2} ' 'is ' f'{result}')

