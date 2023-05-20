# Question 7
# Defining function


def top_performer(data_array, s=0):
    for _ in range(len(data_array)):
        s += data_array[_]
    return s


def standard_dev(data_array, s=0, sum_total=0):
    for _ in range(0, len(data_array)):
        sum_total += data_array[_]
    avr = sum_total / len(data_array)
    for _ in range(0, len(data_array)):
        su = (data_array[_] - avr)
        s += pow(su, 2)
    s = s / (len(data_array) - 1)
    return pow(s, 0.5)


# __main__
# Initializing data
asgard_corp = [12, -15, -13, -12, 15, 23, -21, -15, -21, 31, 23, -20]
loki_corp = [13, 11, -12, -16, 19, 24, -21, 16, -27, 35, 29, -20]
stark_corp = [12, 14, -13, -12, 15, 23, 11, 15, -21, 31, 23, -20]
# Printing
print("Program to get top performer")
print("We have past 12 months data of top companies:")
print("Asgard Corporation : ", asgard_corp)
print("Loki Corporation : ", loki_corp)
print("Stark Corporation : ", stark_corp)
print("\nTo calculate top performing stock we must see net gain/loss and Standard Deviation through data")
print("\nAsgard Corporation has", top_performer(asgard_corp), "gain/loss and", standard_dev(asgard_corp),
      "Standard Deviation")
print("\nLoki Corporation has", top_performer(loki_corp), "gain/loss and", standard_dev(loki_corp),
      "Standard Deviation")
print("\nStark Corporation has", top_performer(stark_corp), "gain/loss and", standard_dev(stark_corp),
      "Standard Deviation")
