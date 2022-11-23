N = [[9, 1, 7],
[3, 5, 6],
[4, 7, 8]]

M = [[2, 3, 5, 6],
[8, 9, 1, 2],
[4, 5, 9, 3]]

result = [[0, 0, 0, 0],
[0,0,0,0],
[0,0,0,0]]

for u in range(len(N)):
    for o in range(len(M[0])):
        for p in range(len(M)):
            result[u][o] += N[u][p] * M[p][o]
for d in result:
    print(d)
