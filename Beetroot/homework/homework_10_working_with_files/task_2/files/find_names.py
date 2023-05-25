from typing import Dict, List, Optional

def find_name(book: Dict[str, Dict[str, str]], *args: str) -> None:
    """Функція, що шукає за ім'ям та прізвищем"""
    if not args:
        return None
    result: Dict[str, Dict] = {phone: {} for phone in book}
    name_number: int = 0
    name_dict: Dict[str, str] = {'first_name': "ім'я", 'last_name': "прізвище"}
    name_list: List[Optional[str]] = []
    for arg in args:
        name: str = input(f'Введіть {name_dict[arg]} власника номера: ')
        if name.isalpha():
            name_list.append(name)
        else:
            print(f'Введіть коректне {name_dict[arg]} для пошуку, а не <{name}>.')
            return None
        for phone, value in book.items():
            if value[arg] == name:
                dict_n: Dict[str, str] = result[phone]
                dict_n[arg] = name
        if len(args) == 2:
            for phone, value_ in result.items():
                if len(value_) == 2:
                    name_number += 1
                    print(f'{result[phone]["first_name"]} {result[phone]["last_name"]} має телефон +380{phone}.')
        elif len(args) == 1:
            for phone, value__ in result.items():
                if len(value__) == 1:
                    name_number += 1
                    print(f'{book[phone]["first_name"]} {book[phone]["last_name"]} має телефон +380{phone}.')
            if name_number > 1:
                print(f'На це {name_dict[arg]} є декілька зареєстрованих власників. Оберіть інший критерій пошуку.')
    if name_number == 0:
        print('Вибачте, щодо Вашого запиту в телефонній книзі збігів  не знайдено.')


if __name__ == '__main__':
    our_book = {'979979791': {'first_name': 'Ivan', 'last_name': 'Sirko', 'city': 'Zaporizhzha', 'country': 'Ukraine'},
                '505005051': {'first_name': 'Ivan', 'last_name': 'Mazepa', 'city': 'Subotiv', 'country': 'Ukraine'},
                '969669691': {'first_name': 'Bogdan', 'last_name': 'Khmelnitskiy', 'city': 'Kyiv',
                              'country': 'Ukraine'},
                '888888881': {'first_name': 'Dmytro', 'last_name': 'Jarosh', 'city': 'Kolomyja', 'country': 'Ukraine'}}
    find_name(our_book, 'first_name', 'last_name')
    find_name(our_book, 'first_name')
    find_name(our_book, 'last_name')
