# Question 11
from datetime import datetime

# List of tuples containing start and end timestamps of user sessions
timestamps = [
    (datetime(2022, 5, 1, 10, 0, 0), datetime(2022, 5, 1, 10, 30, 0)),
    (datetime(2022, 5, 1, 11, 0, 0), datetime(2022, 5, 1, 11, 45, 0)),
    (datetime(2022, 5, 1, 12, 0, 0), datetime(2022, 5, 1, 12, 15, 0)),
]

# Calculate total duration and number of sessions
total_duration = sum((end - start).total_seconds() for start, end in timestamps)
num_sessions = len(timestamps)

# Calculate average duration
average_duration = total_duration / num_sessions

# Print average duration
print(f"Average session duration: {average_duration} seconds")