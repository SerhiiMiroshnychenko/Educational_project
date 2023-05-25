def hotkeys() -> None:
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


if __name__ == '__main__':
    hotkeys()
