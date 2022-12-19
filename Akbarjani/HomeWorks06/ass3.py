import numpy as np
a = np.array([[20,10],[17,22]])
b = np.array([350,500])
x = np.linalg.solve(a,b)
print("X = ",x[0],",Y = ",x[1])
