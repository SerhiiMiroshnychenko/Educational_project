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

