# Question 7
print("Program to display number on specific criteria")
# Taking input from the user
num = int(input("Enter a number you want to compare: "))

# Classify the number based on the criteria and printing
if num < 2:
    print("The number", num, "is SMALL")
elif num < 10:
    print("The number", num, "is MEDIUM")
else:
    print("The number", num, "is LARGE")
