import random
import logging

def generate_number():
    return random.randint(1000, 10000)

def main():
    logging.basicConfig(level=logging.DEBUG,  # Set the logging level
        format='%(message)s',) 

    logging.info('Welcome to the Mastermind Game!')

    number = generate_number()

    guessed_number = int(input("Guess the 4 digit number:"))

    if (number == guessed_number):
        logging.info("Great! You guessed the number in just 1 try! You're a Mastermind!")

    else:
        count1 = 0 # Counter 1

        while number != guessed_number:
            count1 += 1 # Incrementing counter 1
            count2 = 0 # Counter 2

            number = str(number)
            guessed_number = str(guessed_number)

            correct = []

            for i in range(0, 4):            
                if (guessed_number[i] == number[i]): # checking for equality of digits
                    count2 = count2 + 1 # number of digits guessed correctly increments
                    
                    correct.append(number[i])

                else:
                    continue

            if (count2 < 4) and (count2 != 0):
                print("Not quite the number. But you did get ", count2, " digit(s) correct!")
                logging.info("Also these numbers in your input were correct.")
 
                for k in correct:
                    print(k, end=' ')
 
                print('\n')
                print('\n')

                guessed_number = int(input("Enter your next choice of numbers: "))

            elif(count2 == 0):
                print("None of the numbers in your input match.")
                guessed_number = int(input("Enter your next choice of numbers: "))

        if number == guessed_number:
            logging.info("You've become a Mastermind!")
            print("It took you only", count1, "tries.")

if __name__ == "__main__":
    main()