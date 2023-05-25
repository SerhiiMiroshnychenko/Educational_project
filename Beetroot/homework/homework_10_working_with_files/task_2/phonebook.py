"""
Extend Phonebook application
Functionality of Phonebook application:
Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application,
 else raise an error. After the user exits, all data should be saved to loaded JSON.
"""
from typing import Dict, Optional

from files.book_operations import open_book, rewrite_book  # type: ignore
from files.hotkeys import hotkeys  # type: ignore
from files.find_names import find_name  # type: ignore
from files.by_phone_number import by_phone_number  # type: ignore
from files.find_city import find_city_country  # type: ignore
from files.cheet import show_phonebook  # type: ignore
from files.say_thanks import say_thanks  # type: ignore


sample_book: Dict[str, Dict[str, str]] = {'979979797': {'first_name': 'Ivan', 'last_name': 'Sirko',
                                        'city': 'Zaporizhzha', 'country': 'Ukraine'},}
def phonebook(bookname: str) -> None:
    """Phonebook application"""
    print('\n', '\t'*4, '<<<Вас вітає "PHONEBOOK"!>>>')
    hotkeys()  # Виводить варіанти команд
    book_: Optional[Dict[str, Dict[str, str]]] = open_book(bookname)  # відкриває файл і створює словник
    book: Dict[str, Dict[str, str]] = book_ or sample_book
    while True:
        choice: str = input('Ваш вибір: ')  # вибір функції
        match choice:
            case 'q':
                say_thanks()
                break
            case 'a':
                by_phone_number(book, 'add_number')
                book = rewrite_book(bookname, book) or book
            case 'ff':
                find_name(book, 'first_name')
            case 'fl':
                find_name(book, 'last_name')
            case 'f':
                find_name(book, 'first_name', 'last_name')
            case 'fn':
                by_phone_number(book, 'find')
            case 'd':
                by_phone_number(book, 'del')
                book = rewrite_book(bookname, book) or book
            case 'rw':
                by_phone_number(book, 'add_info')
                book = rewrite_book(bookname, book) or book
            case 'fc':
                find_city_country(book, 'city')
            case 'fs':
                find_city_country(book, 'country')
            case 'p':
                show_phonebook(book)
            case _:
                print(f'Не дійсний вибір. Функція <{choice}> наразі недоступна.')


if __name__ == '__main__':
    phonebook('files/phonebook.json')
