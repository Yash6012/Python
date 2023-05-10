# Question 2
import math
# defining the function


def max_angular_disp(angular_di, length):
    d = 9.81 / length
    c = math.acos(d)
    return angular_di * c


# __main__
print("Program to calculate the \"The Maximum Angular Displacement\"")
print("Enter \" Any Alphabet (NO) \" to stop entering")
# Taking input from user
while True:
    try:
        le = float(input("Enter the Length of the string: "))
        ang_disp = float(input("Enter the Angular Displacement of the Pendulum: "))
        print("\n\"The Maximum Angular Displacement\" is:", max_angular_disp(ang_disp, le))
    except:
        print("Stopping the program")
        exit()
