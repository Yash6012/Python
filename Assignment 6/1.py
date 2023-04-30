# Question 1
print("Program to print the data of students in ascending order")

# Initialising variable
my_list = []

# Taking user input for number of data to be entered
n = int(input("Enter the number data of students you want to enter:"))
for i in range(0, n):
    name = input("Enter the name of student:")
    age = input("Enter the age of student:")
    height = input("Enter the height of student:")
    # Putting the values obtained in tuple
    tup = (name, age, height)
    # Appending the tuple in list
    my_list.append(tup)

# Printing the initial list
print("The list without sorting is:", my_list)

# Printing the list after sorting it
my_list.sort()
print("\nThe list after sorting is:", my_list)
