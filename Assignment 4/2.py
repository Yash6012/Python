# Question 2
import numpy as np
print("System of three equations are:")
print("-2x+5y+7z = -17.5")
print("3x-6y+2z = 40.6")
print("9x-3y+8z = 56.2")

# Define the coefficients of the system
A = np.array([[-2, 5, 7],
              [3,-6, 2],
              [9, -3, 8]])
b = np.array([-17.5, 40.6, 56.2])

# Solve the system of equations
x = np.linalg.solve(A, b)
print("Solution for the system of equations are:")
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])
