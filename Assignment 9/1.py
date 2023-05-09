# Question 1
# Taking input from user of problems solved
p1 = int(input("Enter the problems practiced in the first week"))
p2 = int(input("Enter the problems practiced in the second week"))
p3 = int(input("Enter the problems practiced in the third week"))
p4 = int(input("Enter the problems practiced in the fourth week"))

# Initializing the variable
c = 0
d = [p1, p2, p3, p4]

# algorithm (it adds 1 to c if target is complete)
for i in range(0, 4):
    if d[i] >= 10:
        print("A complete his target for", i + 1, "th week")
        c += 1

print("\n\nA complete his target for", c, "weeks")
