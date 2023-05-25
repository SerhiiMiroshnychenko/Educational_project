import json
from typing import Dict


def show_phonebook(book: Dict[str, Dict[str, str]]) -> None:
    """Функція, що демонструє поточну структуру телефонної книги"""
    print(json.dumps(book, sort_keys=True, indent=4))


if __name__ == '__main__':
    with open('phonebook.json', encoding='utf-8') as file:
        book1 = json.load(file)
    show_phonebook(book1)
