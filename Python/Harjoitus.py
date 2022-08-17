import random

list1 = "rock", "scissors", "paper"

item = input("rock, scissors, paper?\n")

random_item = random.choice(list1)

print(random_item)

if item == "rock" and random_item == "paper" or item == "paper" and random_item == "scissors" or item == "scissors" \
        and random_item == "rock":
    print("Computer won!")

if item == "rock" and random_item == "scissors" or item == "scissors" and random_item == "paper" or item == "paper" \
        and random_item == "rock":
    print("You won!")

if item == random_item:
    print("It's a tie!")