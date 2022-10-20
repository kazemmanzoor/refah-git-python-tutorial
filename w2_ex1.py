def divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False
        

def print_result(my_func):
    if my_func == True:
        print('divisible')
    else:
         print('not divisible')

n_1 = float(input('enter 1st number: '))
n_2 = float(input('\nenter 2nd number: '))

func = divisible(n_1, n_2)
print_result(func)
