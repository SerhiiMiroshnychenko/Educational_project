# Task 2
# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and
# is only 10 characters long. Print a suitable message depending on the outcome
# of the string evaluation.

phone_number = input('Введіть телефонний номер: ')
print('Формат вірний, все добре!' if phone_number.isdigit() and len(phone_number) == 10 else 'Номер не коректний...')
