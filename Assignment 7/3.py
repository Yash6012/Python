# Question 3
def triangle(height):
    i = 0
    while i < height:
        j = 0
        while j <= i:
            print("*", end="")
            j += 1
        print()
        i += 1


# __main__
# Taking input of height from user
x = int(input("Enter the height of triangle:"))
print("The triangle made of asterisks of Height \"", x, "\" is")
# Calling the function
triangle(x)
