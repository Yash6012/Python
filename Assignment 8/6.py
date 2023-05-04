# Question 6
# Initializing variable
s = 0
n = 1
# Running till it finds a value
while True:
    s += n
    n += 1
    if s % 111 == 0:
        print("The integers goes from 1, 2, 3, ....", n - 1, "and the sum obtained is:", s)
        break
