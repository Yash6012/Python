# Question 11

# Taking input from user
first = eval(input("Enter the first number"))
second = eval(input("Enter the second number"))

# Checking if the number is an integer and then printing its sum
if isinstance(first, int) and isinstance(second, int):
    print("Addition of First", first, "and Second", second, "integer is :", first + second)
else:
    print("Kindly enter integers")
