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
import json
import os

def hotkeys():
    """Функція, що показує правила користування"""
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ['Опис дії', 'Гарячі клавіші']
    table.add_row(['Додавання нових записів (add)', 'a'])
    table.add_row(['Пошук за іменем (first)', 'ff'])
    table.add_row(['Пошук за прізвищем (last)', 'fl'])
    table.add_row(["Пошук за повним ім'ям (find)", 'f'])
    table.add_row(['Пошук за номером телефону (number)', 'fn'])
    table.add_row(['Пошук по місту (city)', 'fc'])
    table.add_row(['Пошук по країні (state)', 'fs'])
    table.add_row(['Видалити запис за заданим номером телефону (del)', 'd'])
    table.add_row(['Оновити запис за заданим номером телефону (rewrite)', 'rw'])
    table.add_row(['Роздрукувати телефонну книгу (print)', 'p'])
    table.add_row(['Вихід з програми (quit)', 'q'])
    print(table)

class BookNotFoundError(BaseException):
    def __init__(self, bookname):
        super(BookNotFoundError, self).__init__()
        self.msg = f"Телефона книга <{bookname}> не знайдена: перевірте ім'я та розташування."

    def __str__(self):
        return self.msg

def open_book(bookname):
    """The function that open phonebook"""
    if os.path.exists(bookname):
        try:
            with open(bookname, encoding='utf-8') as file:
                book = json.load(file)
            return book
        except Exception as err:
            print(f'\nПомічена помилка: {err.__class__}.')
            print('Причина:', err)
    else:
        try:
            raise BookNotFoundError(bookname)
        except BookNotFoundError as err:
            print(err)
            return None

def dump_book(bookname, book: dict):
    """The function that rewrite phonebook"""
    try:
        with open(bookname, 'w', encoding='utf-8') as file:
            json.dump(book, file, sort_keys=True, indent=4)
    except Exception as err:
        print(f'\nПомічена помилка: {err.__class__}.')
        print('Причина:', err)

def rewrite_book(bookname, book: dict):
    """Функція перезапису телефонної книги"""
    try:
        dump_book(bookname, book)
        if book := open_book(bookname):
            return book
    except Exception as err:
        print(f'\nПомічена помилка: {err.__class__}.')
        print('Причина:', err)

def say_thanks():
    """Подякуємо користувачу"""
    print('_' * 20, 'Дякую за користування!', '<Close program>', '^' * 20, sep='\n')

def by_phone_number(book: dict, arg):
    """Базова функція для операцій по телефонному номеру"""
    phone_number = input('Введіть номер телефона: +380')
    if check_number(phone_number):
        match arg:
            case 'find':
                find_number(book, phone_number)
            case 'del':
                del_number(book, phone_number)
            case 'add_number':
                add_data(book, phone_number, 'add_number')
            case 'add_info':
                add_data(book, phone_number, 'add_info')
    else:
        print('Не вірний формат номера: введіть лише 9 цифр')

def find_number(book: dict, phone_number: str):
    """Пошук по номеру телефона"""
    if phone_number in book:
        print(f"Цей номер телефона має {book[phone_number]['first_name']}"
              f" {book[phone_number]['last_name']} "
              f"із {book[phone_number]['city']}")
    else:
        print(f'Номер <+380{phone_number}> не зареєстровано у телефонній книзі.')

def del_number(book: dict, phone_number: str):
    """Видалення номеру телефона"""
    if phone_number in book:
        del book[phone_number]
        print(f'Номер <+380{phone_number}> видалено з телефонної книги.')
    else:
        print(f'Номер <+380{phone_number}> не зареєстровано у телефонній книзі.')

def add_data(book: dict, phone_number: str, arg):
    """Функція, що додає інформацію"""
    if arg == 'add_number':
        if phone_number in book:
            print('Номер вже існує. Оберіть іншу дію чи інший номер.')
            return None
        first_name = input('Введіть ім\'я власника номера: ')
        last_name = input('Введіть прізвище власника номера: ')
        city = input('Введіть місто звідки власник номера: ')
        country = input('Введіть країну звідки власник номера: ')
        if first_name.isalpha() and last_name.isalpha() and city.isalpha():
            book[phone_number] = {'first_name': first_name.capitalize(),
                                  'last_name': last_name.capitalize(),
                                  'city': city.capitalize(),
                                  'country': country.capitalize()
                                  }
            print(f"Тепер цей номер телефона має {book[phone_number]['first_name']}"
                  f" {book[phone_number]['last_name']} "
                  f"із міста {book[phone_number]['city']} ({book[phone_number]['country']}).")
        else:
            print('Не вірний формат вводу. Щасти наступного разу.')
    elif arg == 'add_info':
        if phone_number in book:
            data = {phone_number: book[phone_number]}
            info = input_data(phone_number, data, book)
            show_result(info)
            book.update(info)
        else:
            print(f'Номер <+380{phone_number}> не зареєстровано у телефонній книзі.')

keys = ['phone_number', 'first_name', 'last_name', 'city', 'country']
values = ['номер телефону', 'ім\'я', 'прізвище', 'місто', 'країна']

def input_data(phone_number: str, data: dict, book: dict) -> dict:
    """Функція для оновлення інформації за номером"""
    new_number = phone_number
    for key, value in zip(keys, values):
        if key == 'phone_number':
            new_number = input(f'Оновіть номер: +380')
            if check_number(new_number):
                del book[phone_number]
                data[new_number] = data[phone_number]
                del data[phone_number]
                print(f'Номер змінено:\n\tбуло: <+380{phone_number}>\n\tстало: <+380{new_number}>')
            else:
                print('Не вірний формат вводу. Номер не буде змінено.')
                new_number = phone_number
        else:
            value = input(f'Оновіть {value}: ')
            if value.isalpha():
                data[new_number][key] = value.capitalize()
    return data

def show_result(info: dict):
    """Функція показу інформації про зміни в телефонній книзі"""
    print('Інформація про зміни:', '_' * 20, sep='\n')
    phone = [key for key in info.keys()][0]
    for key, value in zip(keys, values):
        if key == 'phone_number':
            print(f'{value.capitalize()}: +380{phone}')
        else:
            print(f'{value.capitalize()}: {info[phone][key]}')
    print('^' * 20)

def check_number(phone_number):
    """Перевірка формату телефонного номера"""
    import re
    pattern = r'\d{9}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

def show_phonebook(book: dict):
    """Функція, що демонструє поточну структуру телефонної книги"""
    print(json.dumps(book, sort_keys=True, indent=4))

def find_city_country(book: dict, arg):
    """Пошук за містом чи країною"""
    dict_values = {'city': 'місто', 'country': 'країну'}
    d_values = {'city': 'місті', 'country': 'країні'}
    new_value = input(f'Введіть {dict_values[arg]}: ')
    if new_value.isalpha():
        counter = 0
        for phone in book:
            if book[phone][arg] == new_value:
                counter += 1
                print(f"В {d_values[arg]} {new_value} зареєстровано {book[phone]['first_name']} "
                      f"{book[phone]['last_name']} з номером +380{phone} ")
        print(f'Кількість записів за Вашим запитом: {counter}.' if counter > 0
              else 'За Вашим запитом записів не знайдено.')
    else:
        print(f'Не коректний ввід. Спробуйте ще.')

def find_name(book: dict, *args):
    """Функція, що шукає за ім'ям та прізвищем"""
    name_dict = {'first_name': "ім'я", 'last_name': "прізвище"}
    name_list = []
    if args:
        result = {phone: {} for phone in book}
        name_number = 0
        for arg in args:
            name = input(f'Введіть {name_dict[arg]} власника номера: ')
            if name.isalpha():
                name_list.append(name)
            else:
                print(f'Введіть коректне {name_dict[arg]} для пошуку, а не <{name}>.')
                return None
            for phone in book:
                if book[phone][arg] == name:
                    dict_n = result[phone]
                    dict_n[arg] = name
            if len(args) == 2:
                for phone in result:
                    if len(result[phone]) == 2:
                        name_number += 1
                        print(f'{result[phone]["first_name"]} {result[phone]["last_name"]} має телефон +380{phone}.')
            elif len(args) == 1:
                for phone in result:
                    if len(result[phone]) == 1:
                        name_number += 1
                        print(f'{book[phone]["first_name"]} {book[phone]["last_name"]} має телефон +380{phone}.')
                if name_number > 1:
                    print(f'На це {name_dict[arg]} є декілька зареєстрованих власників. Оберіть інший критерій пошуку.')
        if name_number == 0:
            print('Вибачте, щодо Вашого запиту в телефонній книзі збігів  не знайдено.')

def set_new_book():
    import json
    new_book = {'979979797': {'first_name': 'Ivan', 'last_name': 'Sirko', 'city': 'Zaporizhzha', 'country': 'Ukraine'},
                '505005050': {'first_name': 'Ivan', 'last_name': 'Mazepa', 'city': 'Subotiv', 'country': 'Ukraine'},
                '969669696': {'first_name': 'Bogdan', 'last_name': 'Khmelnitskiy', 'city': 'Kyiv',
                              'country': 'Ukraine'},
                '888888888': {'first_name': 'Dmytro', 'last_name': 'Jarosh', 'city': 'Kolomyja', 'country': 'Ukraine'}}

    with open('phonebook.json', 'w', encoding='utf-8') as f:
        json.dump(new_book, f, sort_keys=True, indent=4)

def phonebook(bookname):
    """Phonebook application"""
    print('\n', '\t'*4, '<<<Вас вітає "PHONEBOOK"!>>>')
    hotkeys()  # Виводить варіанти команд
    book = open_book(bookname)  # відкриває файл і створює словник
    while True:
        choice = input('Ваш вибір: ')  # вибір функції
        match choice:
            case 'q':
                say_thanks()
                break
            case 'a':
                by_phone_number(book, 'add_number')
                book = rewrite_book(bookname, book)
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
                book = rewrite_book(bookname, book)
            case 'rw':
                by_phone_number(book, 'add_info')
                book = rewrite_book(bookname, book)
            case 'fc':
                find_city_country(book, 'city')
            case 'fs':
                find_city_country(book, 'country')
            case 'p':
                show_phonebook(book)
            case _:
                print(f'Не дійсний вибір. Функція <{choice}> наразі недоступна.')

if __name__ == '__main__':
    set_new_book()
    phonebook('phonebook.json')
