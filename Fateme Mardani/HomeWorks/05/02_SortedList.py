def func(a):
    newlist = []
    for item in a:
        sortedList = list(reversed(sorted(item)))
        newlist.append(sortedList)
    return newlist

m = int(input('Number of rows, m = '))
n = int(input('Number of columns, n = '))
input_list2d = []; columns = []
# initialize the number of rows
for i in range(0,m):
  input_list2d += [0]
# initialize the number of columns
for j in range (0,n):
  columns += [0]
# initialize the matrix
for i in range (0,m):
  input_list2d[i] = columns
for i in range (0,m):
  for j in range (0,n):
    print ('Entry in row: ',i+1,' column: ',j+1)
    input_list2d[i][j] = int(input())
    
output = func(input_list2d)
print("Sorted list:",output)
