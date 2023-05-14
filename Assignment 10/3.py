# Question 2
import math


def angular_disp(i_ang_disp, le, init_vel, time):
    a = math.cos((math.sqrt(9.81 / le)) * time)
    b = init_vel / (math.sqrt((9.81 / le)))
    c = math.sin((math.sqrt(9.81 / le)) * time)
    return a + (b * c)


# __main__
# Taking input from user
init_a_disp = float(input("Enter the initial Angular Displacement of the pendulum (in radians): "))
length = float(input("Enter the length of the pendulum (in meters): "))
init_v = float(input("Enter the initial velocity (in meters/second): "))
t = float(input("Enter the time taken (in seconds): "))
result = angular_disp(init_a_disp, length, init_v, t)
print("The Angular displacement is ", round(result, 2), "radians")
if result < 0:
    print("The displacement is in \"opposite direction\" as the negative sign suggests")
