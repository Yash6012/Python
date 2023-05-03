# Question 6
# Defining the pairs
def pair_1():
    # Creating values of r and w in global scope
    global r1, w1
    r1 = 1002
    w1 = 3222


def pair_2():
    # Creating values of r and w in global scope
    global r2, w2
    r2 = 789
    w2 = 3222


def pair_3():
    # Creating values of r and w in global scope
    global r3, w3
    r3 = 300
    w3 = 233


def comp(r, w):
    if r > w:
        print("For this pair there are", r, "Red and", w, "White Balls")
        print("There are fewer white balls\n")
    else:
        print("For this pair there are", r, "Red and", w, "White Balls")
        print("There are more white balls\n")


pair_1()
comp(r1, w1)
pair_2()
comp(r2, w2)
pair_3()
comp(r3, w3)
# Initializing the variable
# r = 0
# w = 0
# print(r, w)
# Taking input from user

# r = int(input("Enter the number of red balls:"))
# w = int(input("Enter the number of White balls:"))

