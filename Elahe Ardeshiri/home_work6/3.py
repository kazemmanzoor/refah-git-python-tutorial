
import numpy as np

x = np.array([
             [20 , 10],
             [17 , 22]
                    ])

y = np.array([350 , 500])
result = np.linalg.solve(x , y)
print("orange = ",result[0],"\n narengy = ",result[1])
