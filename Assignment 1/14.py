# Question 14

# Taking input from user
check = int(input("Kindly enter the number whose divisibility is to be checked by fifteen"))

# Checkin the divisibility
if check % 15 == 0:
    print("The number", check, "is divisible by fifteen")
else:
    print("The number", check, "is not divisible by fifteen")
