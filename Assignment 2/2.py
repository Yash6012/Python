# Question 2
print("Python Program calculates the h for a given p")
# Taking input from the user
p = float(input("Kindly enter the pressure in millibars:"))
# Algorithm to calculate h
h = p / 1013.25
h = pow(h, 0.190289)
h = 145366.45 * (1 -h)
print("The altitude is:", h, "ft")
