def list2D(b):
    LSum = []
    for item in b:
        count = 0
        for i in item:
            count = count+i
        LSum.append(count)
    return LSum
    
R= int(input("Enter the number of columns:")) 

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
    	print(end = " ")
    	
print(list2D(matrix))