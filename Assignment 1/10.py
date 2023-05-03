# Question 10
# taking input from users
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm = ""
if num1 > num2:
    greater = num1
else:
    greater = num2
while True:
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
        break
    greater += 1
# printing the result for the users
print("The L.C.M. of", num1, "and", num2, "is", lcm)
