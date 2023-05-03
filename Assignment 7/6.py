# Question 6
# Defining Variable
r1, r2, r3, w1, w2, w3 = 0, 0, 0, 0, 0, 0


# Defining the pairs
def pair_1():
    # Creating values of r1 and w1 in global scope
    global r1, w1
    r1 = 1002
    w1 = 3222


def pair_2():
    # Creating values of r2 and w2 in global scope
    global r2, w2
    r2 = 789
    w2 = 3222


def pair_3():
    # Creating values of r3 and w3 in global scope
    global r3, w3
    r3 = 300
    w3 = 233


# Defining the comp function for comparison
def comp(r, w):
    if r > w:
        print("For this pair there are", r, "Red and", w, "White Balls")
        print("There are fewer white balls\n")
    else:
        print("For this pair there are", r, "Red and", w, "White Balls")
        print("There are more white balls\n")


# __main__
# Calling the function
pair_1()
pair_2()
pair_3()
comp(r1, w1)
comp(r2, w2)
comp(r3, w3)
