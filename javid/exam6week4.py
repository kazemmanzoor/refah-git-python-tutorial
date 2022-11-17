
matrix1 = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]



matrix2 = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]

	

r = [[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]



for i in range(len(matrix1)):
	for j in range(len(matrix2[0])):
		for k in range(len(matrix2)):
			r[i][j] += matrix1[i][k] * matrix2[k][j]
