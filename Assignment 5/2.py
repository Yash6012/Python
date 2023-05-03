# Question 2
import math


# Defining Function
def mhr(x):
    if gender == 'male' or gender == 'Male':
        s = x - 104.3
        d = 0.033 * s
        return 203.7 / 1 + math.e ** d
    elif gender == 'female' or gender == 'Female':
        s = x - 107.5
        d = 0.0453 * s
        return 190.2 / 1 + math.e ** d


# Taking user input
gender = input("Kindly enter your gender(male, Female)")
age = int(input("Kindly enter your Age"))
resting_Heart_rate = float(input("Kindly enter your Resting  Heart Rate"))
fitness_level = input("Kindly enter your Fitness Level (Low,  Medium, High)")
i_l, i_m, i_h = 0.55, 0.65, 0.8
if fitness_level == 'low' or fitness_level == 'Low':
    thr = (mhr(age) - resting_Heart_rate) * i_l + resting_Heart_rate
    print(round(thr))
elif fitness_level == 'medium' or fitness_level == 'Medium':
    thr = (mhr(age) - resting_Heart_rate) * i_m + resting_Heart_rate
    print(round(thr))
elif fitness_level == 'high' or fitness_level == 'High':
    thr = (mhr(age) - resting_Heart_rate) * i_h + resting_Heart_rate
    print(round(thr))
else:
    print("Invalid input")
