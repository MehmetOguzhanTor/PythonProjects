import random
import logging

def generate_number(number_of_digits):
    return random.randint(1, 10**number_of_digits)

def main():
    logging.basicConfig(level=logging.DEBUG,  # Set the logging level
        format='%(message)s',) 

    logging.info('Welcome to the Mastermind Game!')
    logging.info('Please enter the number of digits your number will have')


if __name__ == "__main__":
    main()