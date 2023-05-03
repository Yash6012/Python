# Question 3
import random

# generating a random amount to be paid
a = round(random.uniform(0.01, 50.00), 2)
print("Total Amount to be paid: $", a)

# asking user for payment amount
p = float(input("Enter payment ($1, $5, $10, $20, or $50): "))

# calculate change
change = round(p - a, 2)

# calculate number of bills
bills = int(change)
coins = int(round((change - bills) * 100))
fifty_dollar = bills // 50
twenty_dollar = (bills % 50) // 20
ten_dollar = ((bills % 50) % 20) // 10
five_dollar = (((bills % 50) % 20) % 10) // 5
one_dollar = ((((bills % 50) % 20) % 10) % 5) // 1

# calculate number of coins for change
quarters = coins // 25
dimes = (coins % 25) // 10
nickels = ((coins % 25) % 10) // 5
pennies = ((coins % 25) % 10) % 5

# if payment is less than amount to be paid then quiting the  program
if p < a:
    print("Error: payment is less than amount to be paid")
    exit()
print("Change to be given is:")
if fifty_dollar > 0:
    print(fifty_dollar, " $50 bills")
if twenty_dollar > 0:
    print(twenty_dollar, " $20 bills")
if ten_dollar > 0:
    print(ten_dollar, " $10 bills")
if five_dollar > 0:
    print(five_dollar, " $5 bills")
if one_dollar > 0:
    print(one_dollar, " $1 bills")
if quarters > 0:
    print(quarters, " quarters")
if dimes > 0:
    print(dimes, " dimes")
if nickels > 0:
    print(nickels, " nickels")
if pennies > 0:
    print(pennies, " pennies")
