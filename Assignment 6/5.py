# Question 5
# Taking input from user
hour = float(input("Enter the time in hours:"))
rate_per_hour = float(input("Enter the value of rate per hour:"))

# introducing control statement (Algorithm)
if hour > 40:
    extra = (hour - 40) * 1.5 * rate_per_hour
    total = 40 * rate_per_hour + extra
    print("Gross payment for the employee is", total, "rupees")
else:
    print("Gross payment for the employee is", rate_per_hour * hour, "rupees")
