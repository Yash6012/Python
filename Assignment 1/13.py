# Question 13

# Taking input from user
user_inp = str(input("Enter the text you want to be checked:"))
# Checking if the input is numeric
while user_inp.isnumeric():
    print("The input", user_inp, "is numeric")
    break
else:
    print("The input", user_inp, "is not numeric")
    exit()
