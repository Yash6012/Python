# Question 15
# Defining function


def more(m, f):
    data = []
    for _ in range(len(male)):
        if m[_] > f[_]:
            data.append(1)
        elif m[_] < f[_]:
            data.append(0)
    return data


# __main__
# Initializing the data
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
male = [650436593, 658420351, 666165661, 673747770, 681223332, 688604687, 695880522, 703055580, 710129572, 717100970,
        723973437, 730746615]
female = [599851346, 607359892, 614676458, 621852998, 628929060, 635912563, 642796257, 649586703, 656288184, 662903415,
          669435596, 675885166]
print("Program to analyze gender distribution in India")
r1 = more(male, female)
print(r1)
for _ in range(len(r1)):
    if r1[_] == 1:
        print("In Year", year[_], "male (", male[_], ") are more than female (", female[_], ")")
