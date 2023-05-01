# Question 4
# Creating the function
def invert_dict(dictionary):
    inverted = {}  # Initializing a variable
    # Parsing the dictionary
    for k, v in dictionary.items():
        inverted[v] = [k]  # adding Key:value pairs in dictionary
    return inverted


# __main__
# Initializing the dictionary
my_dict = {"Harry": "ChosenOne", "Albus": "Phoenix", "Voldemort": "DarkLord", "Severus": "Always",
           "Hermione": "Smartest", "Sirius": "Padfoot"}

# Calling the function
inverted_dict = invert_dict(my_dict)
print("The initial Dictionary is:", my_dict)
print("\nThe Dictionary after inversion:", inverted_dict)
