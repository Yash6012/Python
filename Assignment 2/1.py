# Question 1
print("Python Program to print the BMI of a person")
# Taking input from the user
w = float(input("Kindly enter the weight in pounds:"))
h = float(input("Kindly enter the height in inches:"))

# Algorithm to calculate bmi
h = pow(h, 2)
bmi = 703 * (w / h)
bmi = round(bmi, 10)
print("The BMI is:", bmi)
