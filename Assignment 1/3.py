# Question 3
import datetime
# Printing date
date = datetime.date.today()

print("Today's Date is:", date)

# Printing time

hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)
seconds = int(datetime.datetime.now().second)

print("Time is : - ", hour, ":", minute, ":", seconds)
