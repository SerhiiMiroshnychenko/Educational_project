base_dict = {'phone_number': {'first_name': '',
                              'last_name': '',
                              'city': '',
                              'country': ''}}

keys = ['phone_number', 'first_name', 'last_name', 'city', 'country']
values = ['номер телефону', 'ім\'я', 'прізвище', 'місто', 'країна']


def print_commands():
    print("Доступні команди:",
          "n - створити новий запис",
          "sf - пошук за ім'ям",
          "sl - пошук за прізвищем",
          "sfl - пошук за повним ім'ям",
          "sp - пошук за телефоном",
          "sct - пошук за містом",
          "sc - пошук за країною",
          "up - оновлення запису",
          "del - видалити запис",
          "exit - вихід з програми", sep='\n')


def print_result(result_list):
    for record in result_list:
        for phone in record:
            for key, value in zip(keys, values):
                if key == 'phone_number':
                    print(f'{value.capitalize()}: {phone}')
                else:
                    print(f'{value.capitalize()}: {record[phone][value]}')


def read_values():
    new_data = {}
    phone = ''
    for key, value in zip(keys, values):
        if key == 'phone_number':
            phone = input(f'Введіть {value}: ')
            new_data[phone] = {}
        else:
            new_data[phone][key] = input(f'Введіть {value}: ')
    return new_data


if __name__ == '__main__':
    print(read_values())
