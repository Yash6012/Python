# Question 4
import numpy as np
import matplotlib.pyplot as p

# Define the interval
x = np.linspace(-10, 10)

# Compute the values of the function
y = 3 * x ** 4 + 2 * x ** 3 + 7 * x ** 2 + 2 * x + 9
z = 5 * x ** 3 + 9 * x + 2

# Plot the function
p.plot(x, y)
p.plot(x, z)

# Add labels
p.xlabel('x')
p.ylabel('y')
p.title('Function f(x)')

# Show the plot
p.show()
