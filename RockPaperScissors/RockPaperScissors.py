import random

print("Welcome to the Rock, Paper and Scissors Game! \nPlease enter how many rounds we will play the game:")

n_of_rounds = input()

if not n_of_rounds.isnumeric():
    print("You did not give me a valid number. I guess we are not playing...")
    exit()

n_of_rounds = int(n_of_rounds)

print("We are going to play the game ", n_of_rounds, "times!")


game_choices = ["Rock", "Paper", "Scissors"]
computer_score = 0
user_score = 0


for i in range(n_of_rounds):

    
    computer = random.choice(game_choices) 
    user = input("Enter your choice: ").capitalize()

    if computer == user:
        print("Tie!")
    elif computer == "Rock":
        if user == "Paper":
            print("You win!", user, "covers", computer)
            user_score+=1
        else:
            print("You lose!", computer, "smashes", user)
            computer_score+=1

    elif computer == "Paper":
        if user == "Scissors":
            print("You win!", user, "cuts", computer)
            user_score+=1
        else:
            print("You lose!", computer, "covers", user)
            computer_score+=1

    elif computer == "Scissors":
        if user == "Rock":
            print("You win!", user, "smashes", computer)
            user_score+=1
        else:
            print("You lose!", computer, "cuts", user)
            computer_score+=1

if computer_score == user_score:
    print("The Score is: ", computer_score, "-", user_score, "The game was a Tie!")
elif user_score > computer_score:
    print("The Score is: ", computer_score, "-", user_score, "You Won! Congratulations")
else:
    print("The Score is: ", computer_score, "-", user_score, "You lost! HEHE")
