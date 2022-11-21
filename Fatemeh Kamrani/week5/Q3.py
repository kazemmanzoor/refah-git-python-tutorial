R= int(input("Enter the number of columns:")) 
C = int(input("Enter the number of columns:")) 
matrix1 = [] 
print("Enter the entries rowwise:") 
for i in range(R):       
    a =[] 
    for j in range(C): 
         a.append(int(input())) 
    matrix1.append(a) 
for i in range(R): 
    for j in range(C): 
    	print(end = " ")
    	 	
print(matrix1)

A= int(input("Enter the number of columns:")) 
B = int(input("Enter the number of columns:")) 
matrix2 = [] 
print("Enter the entries rowwise:") 
for i in range(A):    
    b =[] 
    for j in range(B): 
         b.append(int(input())) 
    matrix2.append(b) 
for i in range(A): 
    for j in range(B): 
    	print(end = " ")
    	 	
print(matrix2)
 
# retrieving the sizes of the matrices
p = len(matrix1)
q = len(matrix1[0])
 
t = len(matrix2)
r = len(matrix2[0])

if(q!=t):
   print("Error! Matrix sizes are not compatible")
   quit()
 
# creating the product matrix of dimensions p×r
# and filling the matrix with 0 entries
D = []
for row in range(p):
   curr_row = []
   for col in range(r):
       curr_row.append(0)
   D.append(curr_row)
 
 
# performing the matrix multiplication
for i in range(p):
   for j in range(r):
       curr_val = 0
       for k in range(q):
           curr_val + = A[i][k]*B[k][j]
       D[i][j] = curr_val
 
print(D)

#واقعا نمیدونم چطوری مشکلشو حل کنم ارورش توی خط ۵۷ هستش