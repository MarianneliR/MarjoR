import random

list1 = "rock", "scissors", "paper"

item = input("rock, scissors, paper?\n")

random_item = random.choice(list1)

print(random_item)
