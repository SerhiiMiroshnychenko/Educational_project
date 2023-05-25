import json
import os
from typing import Dict, Optional


class BookNotFoundError(BaseException):
    def __init__(self, bookname: str) -> None:
        super(BookNotFoundError, self).__init__()
        self.msg = f"Телефона книга <{bookname}> не знайдена: перевірте ім'я та розташування."

    def __str__(self) -> str:
        return self.msg


def open_book(bookname: str) -> Optional[Dict[str, Dict[str, str]]]:
    """The function that open phonebook"""
    if os.path.exists(bookname):
        try:
            with open(bookname, encoding='utf-8') as file:
                book: Dict[str, Dict[str, str]] = json.load(file)
            return book
        except Exception as err:
            print(f'\nПомічена помилка: {err.__class__}.')
            print('Причина:', err)
            return None
    else:
        try:
            raise BookNotFoundError(bookname)
        except BookNotFoundError as err:
            print(err)
            return None


def dump_book(bookname: str, book: Optional[Dict[str, Dict[str, str]]]) -> None:
    """The function that rewrite phonebook"""
    try:
        with open(bookname, 'w', encoding='utf-8') as file:
            json.dump(book, file, sort_keys=True, indent=4)
    except Exception as err:
        print(f'\nПомічена помилка: {err.__class__}.')
        print('Причина:', err)


def rewrite_book(bookname: str, book: Optional[Dict[str, Dict[str, str]]]) -> Optional[Dict[str, Dict[str, str]]]:
    """Функція перезапису телефонної книги"""
    try:
        dump_book(bookname, book)
        book_: Optional[Dict[str, Dict[str, str]]] = open_book(bookname)
        return book_ if isinstance(book_, dict) else None
    except Exception as err:
        print(f'\nПомічена помилка: {err.__class__}.')
        print('Причина:', err)
        return None


if __name__ == '__main__':
    print(open_book('phonebook.json'))
