# Question 6
import math
# Annualized Volatility = Standard Deviation of Daily Returns * Square Root of Number of Trading Days in a Year
# Defining function


def standard_dev(data_array, s=0, sum_total=0):
    for _ in range(0, len(data_array)):
        sum_total += data_array[_]
    avr = sum_total / len(data_array)
    for _ in range(0, len(data_array)):
        su = (data_array[_] - avr)
        s += pow(su, 2)
    s = s / (len(data_array) - 1)
    return pow(s, 0.5)


def volatility(std_dev, no_days):
    return std_dev * math.sqrt(no_days)


# __main__
print("The program to calculate the annualized volatility of a stock")
# Initializing Variable
d = []
n = int(input("Enter the number of historical stock returns you want to enter : "))
for i in range(n):
    x = float(input("Enter the {} th amount : ".format(i + 1)))
    d.append(x)
print("\nThe data array of historical daily return is: ", d)
n = int(input("\nEnter the number of Trading Days in a Year : "))
r1 = standard_dev(d)
print("The Annualized Volatility of a stock is : ", volatility(r1, n))
