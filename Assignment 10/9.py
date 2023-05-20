# Question 9
# initializing data

time_p = [2017, 2018, 2019, 2020, 2021]
inflation = [3.33, 3.94, 3.73, 6.62, 5.13]

mean_time = sum(time_p)/len(time_p)

inflation_Mean = sum(inflation)/len(inflation)

Observations = len(time_p)

Numerator = (Observations*sum([time_pi*inflationi for time_pi, inflationi in zip(time_p,inflation)]))-(sum(time_p)*sum(inflation))

Denominator = (Observations*sum([time_pi**2 for time_pi in time_p])) - (sum(time_p)**2)
slope = Numerator / Denominator
inter = inflation_Mean - (slope * mean_time)
future_p = float(input("Enter the forecasted period: "))
for_inf = inter + (slope * future_p)
print("Forecasted inflation for period ", future_p, ":", for_inf)
