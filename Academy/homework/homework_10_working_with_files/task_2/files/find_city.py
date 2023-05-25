from typing import Dict

def find_city_country(book: Dict[str, Dict[str, str]], arg: str) -> None:
    """Пошук за містом чи країною"""
    dict_values: Dict[str, str] = {'city': 'місто', 'country': 'країну'}
    new_value: str = input(f'Введіть {dict_values[arg]}: ')
    if new_value.isalpha():
        counter: int = 0
        d_values: Dict[str, str] = {'city': 'місті', 'country': 'країні'}
        for phone in book:
            if book[phone][arg] == new_value:
                counter += 1
                print(f"В {d_values[arg]} {new_value} зареєстровано {book[phone]['first_name']} "
                      f"{book[phone]['last_name']} з номером +380{phone} ")
        print(f'Кількість записів за Вашим запитом: {counter}.' if counter > 0
              else 'За Вашим запитом записів не знайдено.')
    else:
        print('Не коректний ввід. Спробуйте ще.')
