a = [
    [2, 3, 4],
    [3, 4, 5]
]
b = [
    [4, -3, 12],
    [1, 1, 5],
    [1, 3, 2]
]
result = []
r=[]

for j in range(len(a)):
    for i in range(len(b[0])):
        r.append(0)
    result.append(r)
    r=[]



for i in range(len(a)):
   for j in range(len(b[0])):
       for k in range(len(b)):
           result[i][j] += a[i][k] * b[k][j]

for x in result:
   print(x)
