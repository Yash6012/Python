# Question 5
# Creating a function
def word_frequencies(mylist):
    freq = {}  # Creating an empty dictionary
    # Parsing the list
    for item in mylist:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


# __main__
# Initializing a list
my_list = ["Harry", "Albus", "Snape", "Hagrid", "Harry", "Snape", "Albus", "Snape", "Snape", "Sirius", "Hagrid",
           "Sirius", "Remus", "Sirius", "Tonks", "Sirius"]

# Calling the function
s = word_frequencies(my_list)
print("The list is:", my_list)
print("The dictionary with count is:", s)
