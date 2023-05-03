# Question 6
from datetime import date

from_date = date(2023, 7, 20)
to_date = date(2023, 7, 29)

# Calculating Number of days
no_of_days = to_date - from_date

print("No. of days between", from_date, "to", to_date, "are", no_of_days.days)
