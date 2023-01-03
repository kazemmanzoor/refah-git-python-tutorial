import numpy as np

a=np.array([[4,3,2],[-2,2,3],[3,-5,2]])
b=np.array([25,-10,-4])

result=np.linalg.solve(a,b)
print(result[0],result[1],result[2])
