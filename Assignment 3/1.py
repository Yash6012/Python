# Question 1
import random
v = []
c = 0
# Generating a vector of 30 random integers between -20 and 20
for i in range(0, 30):
    x = random.randint(-20, 20)
    # appending it to the list
    v.append(x)
# Find the sum of all elements that are divisible by 3
for i in v:
    if i % 3 == 0:
        c += i
    else:
        continue
print("Vector: ", v)
print("Sum of elements divisible by 3: ", c)
