# Task 1

print("Kindly enter the grades obtained in respective subjects")
s_1 = int(input("Enter the grades obtained in subject 1"))
s_2 = int(input("Enter the grades obtained in subject 2"))
s_3 = int(input("Enter the grades obtained in subject 3"))
s_4 = int(input("Enter the grades obtained in subject 4"))
s_5 = int(input("Enter the grades obtained in subject 5"))

total_marks = s_1 + s_2 + s_3 + s_4 + s_5
average_marks = total_marks / 5
print("The average of the grades are :", average_marks)