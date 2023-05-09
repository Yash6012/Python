# Question 1
import math
# Defining the function to calculate time period


def time_period(length):
    # Initializing constant
    c = 2 * 3.142857
    g = length / 9.8
    r = c * math.sqrt(g)
    return r


# __main__
print("Program to calculate the time period of string")
print("Enter \" Any Alphabet (NO) \" to stop entering length")
# Taking input from user
while True:
    try:
        le = int(input("Enter the Length of the string: "))
        print("\nThe \"Time period\" is:", time_period(le))
    except:
        print("Stopping the program")
        exit()
