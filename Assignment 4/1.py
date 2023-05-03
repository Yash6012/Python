# Question 1
import numpy as np
A = np.array([[1, -1, 2],
              [2, 3, 5],
              [1, 0, 3]])
B = np.array([[1, -1, 2],
              [2, 3, 5],
              [1, 0, 3]])
C = np.array([[1, -1, 2],
              [2, 3, 5],
              [1, 0, 3]])

# Calculating (A+B)*c
print(np.dot(A+B, C))

# Calculating A*C+B*C
x = np.dot(A, C)
y = np.dot(B, C)
print(x + y)
print("True the matrix multiplication is distributive")

# Calculating (A + B)t
print(np.transpose(A + B))

# Calculating At+ Bt
print(np.transpose(A) + np.transpose(B))
print("True (A + B)t= At+ Bt")

# Get the inverse of the matrix
A_inv = np.linalg.inv(A)

# Calculating (B*C)-1
print(np.linalg.inv(B + C))

# Calculating B-1*C-1
print(np.dot(np.linalg.inv(B), np.linalg.inv(C)))
print("False (B*C)-1 is not equal to B-1*C-1")
