# Task 2 - The birthday greeting program.
# Write a program that takes your name as input,
# and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

def greeting():
    """The birthday greeting function"""
    answer = input('Enter your name and age separated by a space: ').split(' ')
    if answer[0].isalpha() and answer[1].isdigit():
        print(f'Hello, {answer[0].capitalize()}! On your next birthday you’ll be {int(answer[1])+1} years.')
    else:
        print('Check if the input is correct.\nTry again:', end=' ')
        greeting()


greeting()
