#sum_rows

def sum_row(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    for i in range(0,rows):
        sumRow=0
        for j in range(0,cols):
    	    sumRow=sumRow+matrix[i][j]
        print( "Sum of"+str(i+1)+"row:"+str(sumRow))
        
matrix=[
	[1,2,3],
	[4,5,6],
	[7,8,9]]
	       
sum_row(matrix)