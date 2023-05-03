# Question 8

# initializing variable
concatenate = ""

lst = ["Hello", "Hola", "Namaste", "Subhodayam"]

# Using for loop for parsing the list
for i in range(0, len(lst)):
    # concatenating elements in string
    concatenate += lst[i]

print('Elements of the list into a string is :', concatenate)
