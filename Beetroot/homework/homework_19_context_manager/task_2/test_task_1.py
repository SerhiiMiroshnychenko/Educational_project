import unittest
from unittest import TestCase
import logging

from ..task_1.task_1 import Open


class TestOpen(TestCase):
    def setUp(self) -> None:
        while True:
            try:
                with open('test.txt', 'w', encoding='utf-8') as f:
                    f.write('Text for test 1.')
                    break
            except PermissionError as error:
                logging.error(f'IN SETUP: {error.__class__} {error}')
        Open.successful_counter = 0
        Open.failed_counter = 0

    def test_Open_read(self):
        """Перевіряємо читання файлу що існує"""
        logging.info('\n\n---------->. test_Open_read START:')
        with Open('test.txt', 'r') as opened_file:
            result1 = opened_file.read()
        result2 = 'Text for test 1.'
        self.assertEqual(result1, result2, msg='Oops!')
        logging.info('\n---------->. test_Open_read END.\n\n')

    def test_Open_write(self):
        """Перевіряємо перезапис файлу"""
        logging.info('\n\n---------->. test_Open_write START:')
        with Open('test.txt', 'w') as opened_file:
            opened_file.write('Text for test 2.')
        with Open('test.txt', 'r') as opened_file:
            result1 = opened_file.read()
        result2 = 'Text for test 2.'
        self.assertEqual(result1, result2, msg='Oops!')
        logging.info('\n---------->. test_Open_write END.\n\n')

    def test_Open_add(self):
        """Перевіряємо дозапис файлу"""
        logging.info('\n\n---------->. test_Open_add START:')
        with Open('test.txt', 'a') as opened_file:
            opened_file.write('Text for test 2.')
        with Open('test.txt', 'r') as opened_file:
            result1 = opened_file.read()
        result2 = 'Text for test 1.Text for test 2.'
        self.assertEqual(result1, result2, msg='Oops!')
        logging.info('\n---------->. test_Open_add END.\n\n')

    def test_Open_no_file(self):
        """Перевіряємо читання файлу що не існує"""
        logging.info('\n\n---------->. test_Open_no_file START:')
        def test_func(file_name):
            with Open(file_name, 'r') as opened_file:
                result1 = opened_file.read()
                logging.info(f'{result1}')

        self.assertRaises(FileNotFoundError, test_func, 'text.txt')
        logging.info('\n---------->. test_Open_no_file END.\n\n')

    def test_Open_wrong_name_error(self):
        """Перевіряємо читання файлу з невідповідним ім'ям"""
        logging.info('\n\n---------->. test_Open_wrong_name_error START:')
        def test_func(file_name):
            with Open(file_name, 'r') as opened_file:
                result1 = opened_file.read()
                logging.info(f'{result1}')

        self.assertRaises(OSError, test_func, 123)
        logging.info('\n---------->. test_Open_wrong_name_error END.\n\n')

    def test_Open_wrong_name_file_unchanged(self):
        """Перевіряємо незмінність файлу після невідповідної операції"""
        logging.info('\n\n---------->. test_Open_wrong_name_file_unchanged START:')
        with Open('test.txt', 'r') as opened_file:
            result1 = opened_file.read()
        try:
            with Open('test.txt', 'w') as opened_file:
                opened_file.write(wrong_context)
        except (NameError, PermissionError) as error:
            logging.error(f'{error.__class__} {error}\n')
        with Open('test.txt', 'r') as opened_file:
            result2 = opened_file.read()
        self.assertEqual(result1, result2, msg='Oops!')
        logging.info('\n---------->. test_Open_wrong_name_file_unchanged END.\n\n')

    def test_successful_counter_add(self):
        """Перевіряємо правильність додавання successful_counter"""
        logging.info('\n\n---------->. test_successful_counter_add START:')
        self.assertEqual(Open.successful_counter, 0, msg='Oops!')
        try:
            with Open('test.txt', 'r') as opened_file:
                opened_file.read()
            self.assertEqual(Open.successful_counter, 1, msg='Oops!')
        except PermissionError as error:
            self.error_handling(error)

        try:
            with Open('test.txt', 'w') as opened_file:
                opened_file.write('Text for test 1.')
        except PermissionError as error:
            self.error_handling(error)

        try:
            with Open('test.txt', 'a') as opened_file:
                opened_file.write('Text for test 2.')
        except PermissionError as error:
            self.error_handling(error)

        self.assertEqual(Open.successful_counter, 3, msg='Oops!')

        try:
            with Open('test.txt', 'x') as opened_file:
                opened_file.write('Text for test 1.')
        except FileExistsError as error:
            logging.error(f'{error.__class__} {error}\n')
        except PermissionError as error:
            self.error_handling(error)

        self.assertEqual(Open.successful_counter, 3, msg='Oops!')

        Open.successful_counter_add()
        self.assertEqual(Open.successful_counter, 4, msg='Oops!')

        logging.info('\n---------->. test_successful_counter_add END.\n\n')

    @staticmethod
    def error_handling(error):
        logging.critical('Permission error!')
        logging.error(f'{error.__class__} {error}\n')
        Open.successful_counter_add()

    def test_failed_counter_add(self):
        """Перевіряємо правильність додавання failed_counter"""
        logging.info('\n\n---------->. test_failed_counter_add START:')
        self.assertEqual(Open.failed_counter, 0, msg='Oops!')
        try:
            with Open('test1.txt', 'r') as opened_file:
                logging.info(f'{opened_file.read()}')
        except FileNotFoundError as error:
            logging.error(f'{error.__class__} {error}\n')
        self.assertEqual(Open.failed_counter, 1, msg='Oops!')
        try:
            with Open('test.txt', 'x') as opened_file:
                opened_file.write('Text for test 1.')
        except FileExistsError as error:
            logging.error(f'{error.__class__} {error}\n')
        try:
            with Open('test.txt', 'x') as opened_file:
                opened_file.write('Text for test 1.')
        except FileExistsError as error:
            logging.error(f'{error.__class__} {error}\n')
        self.assertEqual(Open.failed_counter, 3, msg='Oops!')
        Open.failed_counter_add()
        self.assertEqual(Open.failed_counter, 4, msg='Oops!')

        logging.info('\n---------->. test_failed_counter_add END.\n\n')

if __name__ == '__main__':
    unittest.main()

