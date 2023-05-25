from typing import Dict

def by_phone_number(book: Dict[str, Dict[str, str]], arg: str) -> None:
    """Базова функція для операцій по телефонному номеру"""
    phone_number: str = input('Введіть номер телефона: +380')
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


def find_number(book: Dict[str, Dict[str, str]], phone_number: str) -> None:
    """Пошук по номеру телефона"""
    if phone_number in book:
        print(f"Цей номер телефона має {book[phone_number]['first_name']}"
              f" {book[phone_number]['last_name']} "
              f"із {book[phone_number]['city']}")
    else:
        print(f'Номер <+380{phone_number}> не зареєстровано у телефонній книзі.')


def del_number(book: Dict[str, Dict[str, str]], phone_number: str) -> None:
    """Видалення номеру телефона"""
    if phone_number in book:
        del book[phone_number]
        print(f'Номер <+380{phone_number}> видалено з телефонної книги.')
    else:
        print(f'Номер <+380{phone_number}> не зареєстровано у телефонній книзі.')


def add_data(book: Dict[str, Dict[str, str]], phone_number: str, arg: str) -> None:
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
            data: Dict[str, Dict[str, str]] = {phone_number: book[phone_number]}
            info: Dict[str, Dict[str, str]] = input_data(phone_number, data, book)
            show_result(info)
            book |= info
        else:
            print(f'Номер <+380{phone_number}> не зареєстровано у телефонній книзі.')


keys = ['phone_number', 'first_name', 'last_name', 'city', 'country']
values = ['номер телефону', 'ім\'я', 'прізвище', 'місто', 'країна']


def input_data(phone_number: str, data: Dict[str, Dict[str, str]], book: Dict[str, Dict[str, str]])\
        -> Dict[str, Dict[str, str]]:
    """Функція для оновлення інформації за номером"""
    new_number: str = phone_number
    for key, value in zip(keys, values):
        if key == 'phone_number':
            new_number = input('Оновіть номер: +380')
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


def show_result(info: Dict[str, Dict[str, str]]) -> None:
    """Функція показу інформації про зміни в телефонній книзі"""
    print('Інформація про зміни:', '_' * 20, sep='\n')
    phone: str = list(info.keys())[0]
    for key, value in zip(keys, values):
        if key == 'phone_number':
            print(f'{value.capitalize()}: +380{phone}')
        else:
            print(f'{value.capitalize()}: {info[phone][key]}')
    print('^' * 20)


def check_number(phone_number: str) -> bool:
    """Перевірка формату телефонного номера"""
    import re
    pattern = r'\d{9}$'
    return bool(re.match(pattern, phone_number))


if __name__ == '__main__':
    book = {
        "505005050": {
            "city": "Subotiv",
            "country": "Ukraine",
            "first_name": "Ivan",
            "last_name": "Mazepa"
        },
        "888888888": {
            "city": "Kolomyja",
            "country": "Ukraine",
            "first_name": "Dmytro",
            "last_name": "Jarosh"
        }, }
    print(input_data('505005050', {'505005050': book['505005050']}, book))
    info1 = {'979979797': {'first_name': 'Ivan', 'last_name': 'Sirko', 'city': 'Zaporizhzha', 'country': 'Ukraine'}}
    show_result(info1)
    while True:
        if number := input('Введіть номер: +380'):
            print(check_number(number))
        else:
            break
