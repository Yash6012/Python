# Question 4
from random import *
# Taking input from user
x = int(input("Enter the number: "))
y = str(x)
if y == y[::-1]:
    print("Your number {} is a Palindrome and you have won".format(x))
else:
    print("Your number {} is not a Palindrome and you have lost".format(x))
