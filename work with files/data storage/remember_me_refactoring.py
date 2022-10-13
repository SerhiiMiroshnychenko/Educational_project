import json


def get_stored_username():
    """Видобути збережене ім'я, якщо таке є."""
    filename = 'user_name.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Привітати користувача на ім'я."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'user_name.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We`ll remember you when you come back, {username}!")


greet_user()
