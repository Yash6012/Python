# Question 12
# Initializing data
# Dictionary containing page visit counts
page_visits = {
    "https://github.com/": 100,
    "https://dodi-repacks.site/": 50,
    "https://www.youtube.com/": 75,
    "http://olamovies.cloud/": 60,
    "https://www.tinkercad.com/": 25
}

# Sort the page visits in descending order
sorted_visits = sorted(page_visits.items(), key=lambda x: x[1], reverse=True)

# Print the most visited pages and their visit counts
print("Program to get most visited sites")
for page, count in sorted_visits:
    print(page, "is visited ", count, "times")
