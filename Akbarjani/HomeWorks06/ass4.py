import numpy as np
a = np.array([[4,3,2],[-2,2,3],[3,-5,2]])
b = np.array([25,-10,-4])
x = np.linalg.solve(a,b)
print("X =",x[0],",Y=",x[1],",Z=",x[2] )