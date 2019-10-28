from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

score = 0

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock" or "rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            score -= 1
        else:
            print("You win!", player, "smashes", computer)
            score += 1
            print("Your score is", score)
    elif player == "Paper" or "paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            score -= 1
        else:
            print("You win!", player, "covers", computer)
            score += 1
            print("Your score is", score)
    elif player == "Scissors" or "scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            score -= 1
        else:
            print("You win!", player, "cut", computer)
            score += 1
            print("Your score is", score)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    if score == 3:
        print("You win!")
        break