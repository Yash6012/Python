# Question 5
t = []
# Find all combinations of a, b, and c that satisfy the Pythagorean theorem
for a in range(1, 51):
    for b in range(a, 51):
        for c in range(b, 51):
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                t.append((a, b, c))
# Displaying the results
for x in t:
    print(x[0], x[1], x[2], sep="\t", end="\n")
