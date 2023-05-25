# Task 1 - String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.

start_string = input('Введіть рядок для маніпуляцій: ')
print(start_string[:2]+start_string[-2:] if len(start_string) >= 2 else ' ')
