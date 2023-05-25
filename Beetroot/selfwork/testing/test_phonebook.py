# Task 2
# Write tests for the Phonebook application, which you have implemented in module 1.
# Design tests for this solution and write tests using unittest library

import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import patch, call
import io

from ...homework_10_working_with_files.task_2.files.book_operations import open_book, rewrite_book, dump_book
from ...homework_10_working_with_files.task_2.files.find_names import find_name
from ...homework_10_working_with_files.task_2.files.by_phone_number\
import by_phone_number, find_number, del_number, add_data, input_data, check_number
from ...homework_10_working_with_files.task_2.files.find_city import find_city_country
from ...homework_10_working_with_files.task_2.files.cheet import show_phonebook
from ...homework_10_working_with_files.task_2.files.say_thanks import say_thanks
from ...homework_10_working_with_files.task_2.files.set_book import set_new_book

from ...homework_10_working_with_files.task_2.phonebook import phonebook

class TestPhonebook(TestCase):

    def setUp(self) -> None:
        set_new_book()

    def test_say_thanks_print(self):
        st = say_thanks
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            st()
        result1 = '____________________\nДякую за користування!\n<Close program>\n^^^^^^^^^^^^^^^^^^^^\n'
        result2 = fake_stdout.getvalue()
        self.assertEqual(result1, result2, msg='Oops!')

    def test_open_book_return_dict(self):
        op = open_book
        self.assertIsInstance(op('phonebook.json'), dict, msg='Oops!')

    def test_open_book_dict(self):
        op = open_book
        dict1 = {
            '979979797': {'first_name': 'Ivan', 'last_name': 'Sirko', 'city': 'Zaporizhzha', 'country': 'Ukraine'},
            '505005050': {'first_name': 'Ivan', 'last_name': 'Mazepa', 'city': 'Subotiv', 'country': 'Ukraine'},
            '969669696': {'first_name': 'Bogdan', 'last_name': 'Khmelnitskiy', 'city': 'Kyiv', 'country': 'Ukraine'},
            '888888888': {'first_name': 'Dmytro', 'last_name': 'Jarosh', 'city': 'Kolomyja', 'country': 'Ukraine'}
        }
        self.assertEqual(op('phonebook.json'), dict1, msg='Oops!')

    def test_check_number(self):
        cn = check_number
        self.assertEqual(cn('888888888'), True, msg='Oops!')

    def test_del_number(self):
        dn = del_number
        dict1 = open_book('phonebook.json')
        dict2 = open_book('phonebook.json')
        self.assertEqual(dict1, dict2, msg='Oops!')
        dn(dict1, '888888888')
        self.assertNotEqual(dict1, dict2, msg='Oops!')
        dict0 = {
            '979979797': {'first_name': 'Ivan', 'last_name': 'Sirko', 'city': 'Zaporizhzha', 'country': 'Ukraine'},
            '505005050': {'first_name': 'Ivan', 'last_name': 'Mazepa', 'city': 'Subotiv', 'country': 'Ukraine'},
            '969669696': {'first_name': 'Bogdan', 'last_name': 'Khmelnitskiy', 'city': 'Kyiv', 'country': 'Ukraine'},
        }
        self.assertEqual(dict0, dict1, msg='Oops!')

    def test_del_number_print(self):
        dn = del_number
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            dn(dict1, '888888888')
        result1 = fake_stdout.getvalue()
        result2 = 'Номер <+380888888888> видалено з телефонної книги.\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_dump_book(self):
        db = dump_book
        op = open_book
        dict1 = open_book('phonebook.json')
        db('phonebook.json', {'1': 2, '2': 3})
        self.assertNotEqual(dict1, op('phonebook.json'), msg='Oops!')
        self.assertEqual(op('phonebook.json'), {'1': 2, '2': 3}, msg='Oops!')

    def test_rewrite_book(self):
        rb = rewrite_book
        op = open_book
        self.assertIsInstance(rb('phonebook.json', {'1': 2, '2': 3}), dict, msg='Oops!')
        self.assertEqual(op('phonebook.json'), {'1': 2, '2': 3}, msg='Oops!')

    def test_find_number_print(self):
        fn = find_number
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            fn(dict1, '888888888')
        result1 = fake_stdout.getvalue()
        result2 = 'Цей номер телефона має Dmytro Jarosh із Kolomyja\n'
        self.assertEqual(result1, result2, msg='Oops!')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            fn(dict1, '888888887')
        result1 = fake_stdout.getvalue()
        result2 = 'Номер <+380888888887> не зареєстровано у телефонній книзі.\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_add_data_return_none_and_no_change_book(self):
        ad = add_data
        dict1 = open_book('phonebook.json')
        dict2 = open_book('phonebook.json')
        self.assertIs(ad(dict2, '888888888', 'add_number'), None, msg='Oops!')
        self.assertEqual(dict1, dict2, msg='Oops!') # Перевірка, що не змінює dict2

    def test_add_data_print_number_exists(self):
        ad = add_data
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            ad(dict1, '888888888', 'add_number')
        result1 = fake_stdout.getvalue()
        result2 = 'Номер вже існує. Оберіть іншу дію чи інший номер.\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_show_phonebook_print(self):
        sp = show_phonebook
        dict1 = {'1': 2, '2': 3}
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            sp(dict1)
        result1 = fake_stdout.getvalue()
        result2 = '{\n    "1": 2,\n    "2": 3\n}\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_find_first_name(self):
        fn = find_name
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with mock.patch('builtins.input', return_value="Bogdan"):
                fn(dict1, 'first_name')
        result1 = fake_stdout.getvalue()
        result2 = 'Bogdan Khmelnitskiy має телефон +380969669696.\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_find_last_name(self):
        fn = find_name
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with mock.patch('builtins.input', return_value="Mazepa"):
                fn(dict1,'last_name')
        result1 = fake_stdout.getvalue()
        result2 = 'Ivan Mazepa має телефон +380505005050.\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_find_first_last_name(self):
        fn = find_name
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with mock.patch('builtins.input', side_effect=['Ivan', 'Mazepa']):
                fn(dict1, 'first_name','last_name')
        result1 = fake_stdout.getvalue()
        result2 = 'Ivan Mazepa має телефон +380505005050.\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_no_find_name(self):
        fn = find_name
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with mock.patch('builtins.input', side_effect=['Kolya', 'Serga']):
                fn(dict1, 'first_name','last_name')
        result1 = fake_stdout.getvalue()
        result2 = 'Вибачте, щодо Вашого запиту в телефонній книзі збігів  не знайдено.\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_find_name_wrong_input(self):
        fn = find_name
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with mock.patch('builtins.input', return_value="123"):
                fn(dict1, 'last_name')
        result1 = fake_stdout.getvalue()
        result2 = 'Введіть коректне прізвище для пошуку, а не <123>.\n'
        self.assertEqual(result1, result2, msg='Oops!')

    def test_find_few_first_name(self):
        fn = find_name
        dict1 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with mock.patch('builtins.input', return_value="Ivan"):
                fn(dict1, 'first_name')
        result1 = fake_stdout.getvalue()
        result2 = "Ivan Mazepa має телефон +380505005050.\nIvan Sirko має телефон +380979979797.\n" \
                  "На це ім'я є декілька зареєстрованих власників. Оберіть інший критерій пошуку.\n"
        self.assertEqual(result1, result2, msg='Oops!')

    def test_add_data_print_change_number_and_book(self):
        ad = add_data
        dict1 = open_book('phonebook.json')
        dict2 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with mock.patch('builtins.input', side_effect=['Kolya', 'Serga', 'Odesa','Ukraine']):
                ad(dict1, '777888999', 'add_number')
        result1 = fake_stdout.getvalue()
        result2 = "Тепер цей номер телефона має Kolya Serga із міста Odesa (Ukraine).\n"
        self.assertEqual(result1, result2, msg='Oops!')
        self.assertNotEqual(dict1, dict2, msg='Oops!')

    def test_add_data_print_no_change_number_and_book(self):
        ad = add_data
        dict1 = open_book('phonebook.json')
        dict2 = open_book('phonebook.json')
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with mock.patch('builtins.input', side_effect=['Kolya', 'Serga', 'Odesa','Ukraine']):
                ad(dict1, '979979797', 'add_number')
        result1 = fake_stdout.getvalue()
        result2 = "Номер вже існує. Оберіть іншу дію чи інший номер.\n"
        self.assertEqual(result1, result2, msg='Oops!')
        self.assertEqual(dict1, dict2, msg='Oops!')

    def test_add_data_add_info_successful(self):
        ...

    def test_add_data_add_info_unsuccessful(self):
        ...

    def test_input_data_successful(self):
        ...

    def test_input_data_unsuccessful(self):
        ...

    def test_show_result(self):
        ...

    def test_by_phone_number(self):
        ...

    def test_find_country_successful(self):
        ...

    def test_find_country_unsuccessful(self):
        ...

    def test_find_city_successful(self):
        ...

    def test_find_city_unsuccessful(self):
        ...

    def test_find_country_city_wrong_input(self):
        ...

    def test_phonebook(self):
        ...

if __name__ == '__main__':
    unittest.main()
