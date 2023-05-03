# Question 4
print("Python Program to print the BMI of a person")

# Taking input from the user
w = float(input("Kindly enter the weight in pounds:"))
h = float(input("Kindly enter the height in inches:"))

# Algorithm to calculate bmi
h = pow(h, 2)
bmi = 703 * (w / h)
bmi = round(bmi, 10)
if bmi < 18.5:
    print("Your BMI Value is", round(bmi, 10), ", which  classifies you as Underweight")
elif 18.5 <= bmi or bmi < 24.9:
    print("Your BMI Value is", round(bmi, 10), ", which classifies you as Normal")
elif 25 <= bmi or bmi < 29.9:
    print("Your BMI Value is", round(bmi, 10), ", which  classifies you as Normal")
elif bmi > 30:
    print("Your BMI Value is", round(bmi, 10), ", which classifies you as Normal")
