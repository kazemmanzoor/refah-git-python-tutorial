## 2nd Question - Enteshare Garma - Mardani

import sys
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

matrix = np.array([[100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
                   
for cycle in range (500):
	for j in range (1,9):
    	for i in range (1,9):
        
        	matrix[i][j] = ((1/4)*((matrix[i+1][j])+(matrix[i-1][j])+(matrix[i][j+1])+(matrix[i1][j-1])))
            
            
plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)          
            
plt.title("Contour of Temperature")
plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)

plt.colorbar()
plt.show()

        


        	
