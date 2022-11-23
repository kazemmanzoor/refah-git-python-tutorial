#descending_sort
def des_sort(a):
    Nlist = []
    for item in a:
        sortedList = list(reversed(sorted(item)))
        print(sortedList)
        Nlist.append(sortedList)
    return Nlist

R= int(input("Enter the number of rows:")) 

C = int(input("Enter the number of columns:")) 

matrix = [] 

print("Enter the entries rowwise:") 

for i in range(R):          # A for loop for row entries 

    a =[] 

    for j in range(C):      # A for loop for column entries 

         a.append(int(input())) 

    matrix.append(a) 

for i in range(R): 

    for j in range(C): 
    	print( end = "")
    	
print(des_sort(matrix))