# Question 6
# Initializing the variable
# r = 0
# w = 0
# Taking input from user
try:
    r = int(input("Enter the number of red balls:"))
    w = int(input("Enter the number of White balls:"))
except:
    exit()

if r > w:
    print("There are fewer white balls")
else:
    print("There are more white balls")
