# Question 1
s_s = [72, 81, 44, 68, 90, 53, 80, 75, 74, 65, 50, 92, 85, 69, 41,  73, 70, 86, 61, 65, 79, 94, 69]
x, su, s = 0, 0, 0

# Calculating average
for i in range(0, len(s_s)):
    x += s_s[i]

av = x / len(s_s)
print(av)

# Calculating sum of squares
for i in range(0, len(s_s)):
    su = (s_s[i] - av)
    s += pow(su, 2)

s = s / (len(s_s) - 1)

# Calculating sum of standard deviation
std_dev = pow(s, 0.5)
print(std_dev)
for i in range(0, len(s_s)):
    if s_s[i] >= (av + 1.3 * std_dev):
        print(s_s[i], "% Letter Grade A")
    elif av + 0.5 * std_dev <= s_s[i] < av + 1.3 * std_dev:
        print(s_s[i], "% Letter Grade B")
    elif av - 0.5 * std_dev <= s_s[i] < av + 0.5 * std_dev:
        print(s_s[i], "% Letter Grade C")
    elif av - 1.3 * std_dev <= s_s[i] < av - 0.5 * std_dev:
        print(s_s[i], "% Letter Grade D")
    elif s_s[i] < av - 1.3 * std_dev:
        print(s_s[i], "% Letter Grade F")
    else:
        print("Error in Data")
