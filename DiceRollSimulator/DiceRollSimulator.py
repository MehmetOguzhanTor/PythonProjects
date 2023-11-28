import random

def roll_dice(lowest,highest): #Dice rolling function
    return random.randint(lowest, highest)

def main(): #main function
    lowest = 1
    highest = 6
    roll_again ="y"


    while roll_again.lower() == "y": #Rolling dice loop
        print("Rolling The Dices...")
        print("The Values are :")

        print(roll_dice(lowest,highest)) #First dice
        print(roll_dice(lowest,highest)) #Second dice

        roll_again = input("Roll the Dices Again? y/n") #Continue?


if __name__ == "__main__":
    main()