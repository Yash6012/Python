# Question 3
print("Slicing the tuple and printing in two different lines")
# Initializing tuple
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# algo
print("The given tuple is:", tup)
length = int(len(tup))
d = int(length/2)
# printing the sliced tuple
print("The first half of the above tuple is:", tup[0:d])
print("The second half of the above tuple is:", tup[d:length])
