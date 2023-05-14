# Question 4

# Taking input from user
x = int(input("Enter the number: "))
# Explicit typecasting to string
y = str(x)
# traversing the string in reverse order with -1 step
if y == y[::-1]:
    print("Your number {} is a \"Palindrome\" and you have won".format(x))
else:
    print("Your number {} is not a \"Palindrome\" and you have lost".format(x))
