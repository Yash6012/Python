# Task 4
# input of numbers
x = int(input("Enter the First number :"))
y = int(input("Enter the Second number :"))
print("Before Swapping: First number =", x, " Second number =", y)
# Code to swap 'x' and 'y'
x = x ^ y
y = x ^ y
x = x ^ y
print("After Swapping: First number =", x, "\n Second number =", y)
