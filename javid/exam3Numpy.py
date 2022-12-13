import numpy as np
A=np.array([[4,3,2],
           [-2,2,3],
           [3,-5,-2]])
B=np.array([25,-10,-4])
print(np.linalg.solve(A,B))
