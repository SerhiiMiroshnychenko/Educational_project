# Task 1 - The Guessing Game.
# Write a program that generates a random number between 1 and 10
# and lets the user guess what number was generated. The result
# should be sent back to the user via a print statement.

import random

the_number = random.randint(1, 10)
print("""
HELLO!
You have to guess the number from 1 to 10
and do it in the minimum number of attempts
STARTED:""")
attempt_counter = 0
while True:
    your_number = input('\nEnter a number from 1 to 10: ')
    if your_number.isdigit():
        attempt_counter += 1
        if int(your_number) < the_number:
            print('Your number is less than guessed,try again.')
        elif int(your_number) > the_number:
            print('Your number is more than guessed,try again.')
        else:
            print(f'CONGRATULATIONS!!! You guessed with {attempt_counter} attempt(s)!')
            break
    elif not your_number:
        print('Please enter something.')
    else:
        print('Please enter numbers from 1 to 10.')
        print(f'The entered symbol "{your_number}" is not a number.)')


