# Question 8
import math
# Defining function


def average(data_array, sum_total=0):
    for i in range(0, len(data_array)):
        sum_total += data_array[i]
    avr = sum_total / len(data_array)
    return avr


def standard_dev(data_array, avr, s=0):
    for i in range(0, len(data_array)):
        su = (data_array[i] - avr)
        s += pow(su, 2)
    s = s / (len(data_array) - 1)
    return pow(s, 0.5)


# __main_
print("Program to print Average, Standard deviation, Maximum Inflation and Minimum Inflation\n")
# Initializing Variable
d = []
n = int(input("Enter the number of inflation data you want to enter : "))
for i in range(n):
    x = float(input("Enter the {} th amount : ".format(i + 1)))
    d.append(x)
print("The data array of past inflation is: ", d)
r1 = average(d)
r2 = standard_dev(d, r1)
print("\nThe Average of Inflation is : ", r1)
print("\nThe Standard Deviation of stock Inflation is : ", r2)
print("\nThe maximum Inflation is : ", max(d))
print("\nThe minimum Inflation is : ", min(d))
