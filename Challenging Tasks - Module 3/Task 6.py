# Task 7
# Taking input
num = int(input("Enter the number you want check:"))
if num == 0:
    print("Number", num, " is Zero")
    exit()
elif num % 5 == 0:
    print("Number", num, " is divisible by 5")
else:
    print("Number", num, " is not divisible by 5")
