# Question 2
# Creating a function for login
def accept_login(user, username, password):
    if username in user:
        if user[username] == password:
            print("The user exists and password is also correct")
            return True
        else:
            print("User exist but password is \"Incorrect\"")
    else:
        return False


# __main__

# Creating user dictionary
user_d = {"Harry": "ItsHarry", "Ronald": "CallmeWeasley", "Snape": "Always", "Dumbledore": "Phoenix",
          "Voldemort": "DarkLord"}

# Taking input from user
user_name = input("Enter the username:")
if user_name in user_d:
    pssd = input("Enter the password:")
    # calling the function
    accept_login(user_d, user_name, pssd)
else:
    print("User does not exist")
