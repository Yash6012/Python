# Question 2
# initialising variables
x = 0
y = 0
print("Program to compute the distance from original position to final position")
n = int(input("Enter the number of steps you want to enter"))
for i in range(0, n):
    # Taking input from user
    direction = input("Enter the direction:(Up ,Down, Left, Right)")
    steps = int(input(f"Enter the number of steps in {direction} Direction"))
    direction = direction.lower()
    # adding the steps to an imaginary x-y canvas
    if direction == 'up':
        y += steps
    elif direction == 'down':
        y -= steps
    elif direction == 'left':
        x -= steps
    elif direction == 'right':
        x += steps

# Calculating the distance
distance = pow(x, 2) + pow(y, 2)
print(f"The distance from (0, 0) to ({x} ,{y}) is ", round(distance ** 0.5))
