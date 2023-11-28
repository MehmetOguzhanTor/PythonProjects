import random

def roll_dice(lowest,highest):
    return random.randint(lowest, highest)

def main():

    lowest = 1
    highest = 6
    roll_again ="y"

    while roll_again.lower() == "y":
        print("Rolling The Dices...")
        print("The Values are :")

        
        print(roll_dice(lowest,highest))

        print(roll_dice(lowest,highest))

        roll_again = input("Roll the Dices Again? y/n") 