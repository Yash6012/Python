# Question 12

# Taking input from the user
kpa = float(input("Input pressure in in kilopascals> "))

# Conversion
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325

# Printing the converted values
print("The pressure in pounds per square inch:", psi, "psi")
print("The pressure in millimeter of mercury:", mmhg, "mm of Hg")
print("Atmosphere pressure:", atm, "atm")
