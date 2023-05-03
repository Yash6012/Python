# Question 3
# Initialize the first three Tribonacci numbers
a, b, c = 0, 1, 1
# Printing the first three Tribonacci numbers
print(a, b, c, end=" ")
# Compute and print the next 22 Tribonacci numbers
for i in range(22):
    d = a + b + c
    print(d, end=" ")
    a, b, c = b, c, d
