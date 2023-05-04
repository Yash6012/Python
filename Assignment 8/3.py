# Question 3

# Defining a function to check prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


# __main__
# Initializing an empty list
mersenne_primes = []

# We know 2 ** 14 is 16384
# So we take range till 15 as after that it will be out of scope
# loop through all possible values of n
for n in range(2, 15):
    # calculate the Mersenne number
    mersenne_num = 2 ** n - 1
    # check if it's prime
    if is_prime(mersenne_num):
        # if so, add it to the list of Mersenne primes
        mersenne_primes.append(mersenne_num)

# print the list of Mersenne primes
print("Mersenne prime numbers between 1 and 10,000:", mersenne_primes)
