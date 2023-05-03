# Question 3
import math

# Taking input from the user
half_life = float(input("Enter the half life of the material (in years): "))
A_not = float(input("Enter the current amount of the material (in lb): "))
t = float(input("Enter the number of years from now for which the amount should be calculated: "))

# calculating the constant k
k = math.log(2) / half_life

# calculate the amount at time t
A = A_not * math.exp(-k * t)

# convert from lb to kg
A = A / 2.20462

# print the result
print("The amount of the material after", t, "years is", A, "kg")
