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
my_dict = {"apple": 1, "banana": 2, "orange": 3, "pear": 4}
# Calling the function
inverted_dict = invert_dict(my_dict)
print(inverted_dict)
