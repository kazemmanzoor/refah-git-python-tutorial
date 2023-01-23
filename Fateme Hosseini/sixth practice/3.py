import numpy as np

A = np.array([
             [20 , 10],
             [17 , 22]
                    ])

B = np.array([350 , 500])
result = np.linalg.solve(A , B)
print("orange = ",result[0],"\nnarengy = ",result[1])
