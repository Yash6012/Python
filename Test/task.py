# Question 5
# Conversion factors
sm_scm = 10000
sm_sin = 1550
sm_sft = 10.7639
sm_syd = 1.19599
sm_acre = 0.000247105

# Taking input from user
v = float(input("Enter the Value of the area: "))
c = input("Enter the current unit of the area (m², cm², in², ft², yd², acre): ")
n = input("Enter the new unit of the area (m², cm², in², ft², yd², acre): ")

# Converting every value to square meters
if c == "m":
    s = v
elif c == "cm":
    s = v / sm_scm
elif c == "in":
    s = v / sm_sin
elif c == "ft":
    s = v / sm_sft
elif c == "yd":
    s = v / sm_syd
elif c == "acre":
    s = v / sm_acre
else:
    print("Invalid data")
    exit()

# Converting it to new unit
if n == "m":
    result = s
elif n == "cm":
    result = s * sm_scm
elif n == "in":
    result = s * sm_sin
elif n == "ft":
    result = s * sm_sft
elif n == "yd":
    result = s * sm_syd
elif n == "acre":
    result = s * sm_acre
else:
    print("Invalid data")
    exit()
print(v, c, " = ", result, n)
