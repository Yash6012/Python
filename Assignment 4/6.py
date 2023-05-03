# Question 6
knots_to_mps = 0.514444
v = 180 * knots_to_mps
t = 30

# Calculate the acceleration
a = v / t

# Calculate the minimum runway length
d = (v / 2) * t

# Print the results
print("The acceleration of the plane is:", round(a, 2), "m/s^2")
print("The minimum runway length required is:", round(d, 2), "meters")
