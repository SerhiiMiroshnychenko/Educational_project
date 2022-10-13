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


def get_new_username():
    """Запитати ім'я користувача."""
    username = input("What is your name? ")
    filename = 'user_name.json'
    with open(filename, 'w') as f:
        json.dump(username, f)


