# Question 2

# Defining a function to check prime Number
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# __main__
# Finding all the safe primes between 1 and 10000
print("Safe prime numbers are:")
for p in range(1, 10000):
    if prime(p) and prime(2 * p + 1):
        print(2 * p + 1)
