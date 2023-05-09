# Question 2
print("Program to sort a numbers in non decreasing order")

# initializing variable
a = []

# initializing a for loop
n = int(input("Enter the number of items you want to enter: "))
for i in range(n):
    x = int(input("Enter the number between 0 to 10^6 :"))
    a.append(x)

print("Ended appending in the list")
print("The list is:", a)
a.sort()
print("The list after sorting in non decreasing order is:", a)
