import numpy as np
a = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
b = np.array([2, -10, -4])
x = np.linalg.solve(a, b)
print (x)
