import numpy as np

x = np.array([
             [4 , 3 , 2],
             [-2 , 2 ,3],
             [3,-5 ,2]
                    ])

y = np.array([25 , -10 ,-4])
result = np.linalg.solve(x , y)
print("X = ",result[0],"\nY = ",result[1],"\n Z = ",result[2] )
