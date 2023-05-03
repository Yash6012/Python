# Question 4

# Taking input from user
print("Python program that calculates V")
P = float(input("Enter the initial investment amount: "))
t = int(input("Enter the number of years: "))
r = float(input("Enter the yearly interest rate (as a decimal): "))
n = int(input("Enter the number of times per year that the interest is compounded: "))

# Algorithm to calculate to v
s = (r / 100) / n
s = 1 + s
s = pow(s, n * t)
V = P * s

# Printing the result
print("The value of a $", P, "investment at a yearly interest rate of", r, "% compounded ", n, "times per year, after",
      t, "years is $", V)
