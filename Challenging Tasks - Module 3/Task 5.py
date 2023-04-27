# Task 5
# Taking input
num = int(input("Enter a number:"))
# Main Algorithm
if num == 0:
    print("Number", num, " is Zero")
    exit()
elif num % 2 == 0:
    print("Number", num, " is Even")
elif num % 2 ==1:
    print("Number", num, " is odd")
else:
    print("Kindly enter valid number")
