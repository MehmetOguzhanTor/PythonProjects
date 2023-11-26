import random
import math

#Determining the range of the game
lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

# Random number is generated
the_number = random.randint(lower_bound, upper_bound)


#Number of guesses that user will have
number_of_guess = round(math.log(abs(upper_bound - lower_bound) + 1, 2))
print("You have {} guess chance to win" .format(number_of_guess))

guessed_number = int()
count = 0

while count < (number_of_guess):

    count = count + 1 

    guessed_number = int(input("Enter your guess: "))

    if guessed_number == the_number:
         print("Congratulations you did it in ", count, " try")
         break
    
    elif guessed_number > the_number:
        if count >= number_of_guess:
            print("The number is" , the_number, ". Better luck next time.")
        else:
            print("Try Again! You guessed too high")
    

    elif guessed_number < the_number:
        if count >= number_of_guess:
            print("The number is" , the_number, ". Better luck next time.")
        else:
            print("Try Again! You guessed too small")
         
