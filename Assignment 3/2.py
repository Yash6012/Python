# Question 2
NYC = [33, 33, 18, 29, 40, 55, 19, 22, 32, 37, 58, 54, 51, 52, 45, 41, 45, 39, 3, 45, 33, 18, 19, 19, 28, 34, 44, 21,
       23, 30, 39]
DEN = [39, 48, 61, 39, 14, 37, 43, 3, 46, 39, 55, 46, 46, 39, 54, 45, 52, 52, 6, 45, 62, 40, 25, 57, 60, 57, 20, 32,
       50, 48, 28]
x, d, a, b, c, avg_nyc, avg_den = 0, 0, 0, 0, 0, 0, 0
# Calculating Average temperature
for i in range(0, 31):
    x += NYC[i]
    d += DEN[i]
    avg_nyc = x / 31
    avg_den = d / 31

print("The average temperature in New York City is:", avg_nyc)
print("The average temperature in Denver, Colorado is:", avg_den)
# Printing if the temperature is above than average
for i in range(0, 31):
    if NYC[i] > avg_nyc:
        a += 1
print("The number of days the temperature above then average in New York City is:", a)
for i in range(0, 31):
    if DEN[i] > avg_den:
        b += 1
print("The number of days the temperature above then average in Denver, Colorado is:", b)
# number of days that the temperature in Denver was higher
for i in range(0, 31):
    if NYC[i] < DEN[i]:
        c += 1
print("The number of days that the temperature in Denver was higher than the temperature in New York is:", c)
