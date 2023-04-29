# Question 6
# Taking input from user
while True:
    score = float(input("Enter the score (between 0.0 to 1.0)"))
    if score > 1.0 or score < 0:
        print("The score", score, "you entered is out of range")
        exit()
    elif score >= 0.9:
        print("Grade \"A\" is assigned to", score)
    elif score >= 0.8:
        print("Grade \"B\" is assigned to", score)
    elif score >= 0.7:
        print("Grade \"C\" is assigned to", score)
    elif score >= 0.6:
        print("Grade \"D\" is assigned to", score)
    else:
        print("Grade \"F\" is assigned to", score)
