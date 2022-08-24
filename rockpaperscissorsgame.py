# Creating a rock paper scissors game in python

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie! Nobody wins!\n")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Paper beats rock. Computer wins!\n")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Rock beats scissors. Player wins!\n")
    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Scissors beats paper. Player wins!\n")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Rock beats scissors. Computer wins!\n")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Scissors beats paper. Computer wins!\n")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Paper beats rock. Player wins!\n")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")