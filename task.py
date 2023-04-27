import numpy as np
x_1 = np.array([[157.5, 5, 1],
                [84.2, 8.6, 1],
                [-25.99, -6.8, 1]])

x_det = np.array([[11.5, 5, 1],
                [3.2, 8.6, 1],
                [-4.5, -6.8, 1]])

det = np.linalg.det(x_1)
det2 = np.linalg.det(x_det)
x_0 = round(det / (2 * det2), 5)
print(det)
print(x_0)
