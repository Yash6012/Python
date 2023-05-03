# Question 4
import random
v = []

# Generate vector of 20 random integers between 10 and 30 (A)
for i in range(0, 20):
    x = random.randint(10, 30)
    # appending it to the list
    v.append(x)
print("Vector: ", v)

# Replace non-even integers with random integers between 10 and 30 (B)
for i in range(len(v)):
    if v[i] % 2 != 0:
        v[i] = random.randint(10, 30)
print("Vector: ", v)

# Repeating the above step (C)
for i in range(len(v)):
    if v[i] % 2 != 0:
        v[i] = random.randint(10, 30)
print("Vector: ", v)

# Replace non-even integers with random integers between10 and 30 until all elements are even (D)
count = 0
while any(x % 2 != 0 for x in v):
    for i in range(len(v)):
        if v[i] % 2 != 0:
            v[i] = random.randint(10, 30)
            count += 1
print("Vector: ", v)
print("The step has taken", count, "iterations to get an even vector", v)
