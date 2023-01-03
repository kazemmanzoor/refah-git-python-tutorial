import numpy as np

a=np.array([[20 ,10 ],[17 ,22 ]])
b=np.array([350 ,500 ])

result=np.linalg.solve(a,b)
print(result[0],result[1])
