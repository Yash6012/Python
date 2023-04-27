# Question 6
import numpy as np
print("The First Equation is", round(pow(-1.2, 3), 2), "a +", round(pow(-1.2, 2), 2), "b +", -1.2, "c + d =", 18.8)
print("The Second Equation is", round(pow(0.2, 3), 3), "a +", round(pow(0.2, 2), 2), "b +", 0.2, "c + d =", 5)
print("The Third Equation is", pow(2, 3), "a +", pow(2, 2), "b +", 2, "c + d =", 16)
print("The Fourth Equation is", round(pow(3.5, 3), 2), "a +", round(pow(3.5, 2), 2), "b +", 3.5, "c + d =", 15)

# set up the matrix and the vector of constants
A = np.array([[-1.2**3, -1.2**2, -1.2, 1],
              [0.2**3, 0.2**2, 0.2, 1],
              [2**3, 2**2, 2, 1],
              [3.5**3, 3.5**2, 3.5, 1]])
b = np.array([18.8, 5, 16, 15])

# solve the system of equations
x = np.linalg.solve(A, b)

# print the constants a, b, c, and d
print("The value of a:", round(x[0], 3))
print("The value of b:", round(x[1], 3))
print("The value of c:", round(x[2], 3))
print("The value of d:", round(x[3], 3))
