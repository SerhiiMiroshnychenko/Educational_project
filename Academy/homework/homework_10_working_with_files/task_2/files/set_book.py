def set_new_book() -> None:
    import json
    new_book = {'979979797': {'first_name': 'Ivan', 'last_name': 'Sirko', 'city': 'Zaporizhzha', 'country': 'Ukraine'},
                '505005050': {'first_name': 'Ivan', 'last_name': 'Mazepa', 'city': 'Subotiv', 'country': 'Ukraine'},
                '969669696': {'first_name': 'Bogdan', 'last_name': 'Khmelnitskiy', 'city': 'Kyiv',
                              'country': 'Ukraine'},
                '888888888': {'first_name': 'Dmytro', 'last_name': 'Jarosh', 'city': 'Kolomyja', 'country': 'Ukraine'}}

    with open('phonebook.json', 'w', encoding='utf-8') as f:
        json.dump(new_book, f, sort_keys=True, indent=4)
