# Question 3
import numpy as np
import matplotlib.pyplot as plt

# Define the interval
x = np.linspace(-np.pi, np.pi, 100)

# Plot the functions
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.plot(x, np.tan(x), label='tan(x)')

# labels and legend in graph
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()
