# Question 14
# Initializing variable
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
age0_14 = [30.53, 30.08, 29.62, 29.14, 28.63, 28.12, 27.60, 27.09, 26.59, 26.11, 25.69]
age15_64 = [64.33, 64.70, 65.06, 65.40, 65.73, 66.05, 66.36, 66.66, 66.93, 67.22, 67.51]
age65_ = [5.24, 5.22, 5.32, 5.46, 5.64, 5.84, 6.04, 6.25, 6.47, 6.67, 6.80]
# Printing the data
for _ in range(len(year)):
    print("In year", year[_])
    print("Age group 0 to 14 is", age0_14[_], "%")
    print("Age group 15 to 64 is", age15_64[_], "%")
    print("Age group 65 plus is", age65_[_], "%")
    print("\n")
