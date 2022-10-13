import json

# Завантажити ім'я користувача, якщо воно вже було збережене.
# В іншому разі запитати ім'я користувача та збережіть його.

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We`ll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
