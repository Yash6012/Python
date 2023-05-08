# Question 1
# Taking input from user of problems solved
p1 = int(input("Enter the problems practiced in the first week"))
p2 = int(input("Enter the problems practiced in the second week"))
p3 = int(input("Enter the problems practiced in the third week"))
p4 = int(input("Enter the problems practiced in the fourth week"))
# Initializing the variable
c = 0

# algorithm (it adds 1 to c if target is complete)
if p1 >= 10:
    c += 1

if p2 >= 10:
    c += 1

if p3 >= 10:
    c += 1

if p4 >= 10:
    c += 1
print("A complete his target for", c, "weeks")
