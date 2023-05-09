# Question 3
n = int(input("Enter the number of rounds played: "))
# Initializing the variables
player1 = 0
player2 = 0
lead = 0
leader = 0
# for loop
for i in range(n):
    print("Round {}".format(i + 1))
    score1 = int(input("Enter the score of player 1: "))
    score2 = int(input("Enter the score of player 2: "))
    player1 += score1
    player2 += score2
    diff = player1 - player2
    diff = abs(diff)
    if player1 > player2 and diff > lead:
        lead = diff
        leader = 1
    if player2 > player1 and diff > lead:
        lead = diff
        leader = 2
print("The leader is player ", leader, "The lead is : ", lead)
