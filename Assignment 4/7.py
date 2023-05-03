# Question 7
a = 0.75
station_length = 184
distance = 1425

# Calculate the cruising speed
speed = ((2 * a * station_length) ** 0.5)
print("The train's cruising speed is:", round(speed, 2), "m/s")

# Calculate the time it took to accelerate to cruising speed
print("The time it took for the train to accelerate to cruising speed is:", round(speed / a, 2), "seconds")

# Calculate the time it takes to travel to the next station
print("The time it takes the train to travel to the next station is:",
      round((distance -station_length) / speed, 2), "seconds")
