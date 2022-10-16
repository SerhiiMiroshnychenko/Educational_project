import unittest
from name_function_2 import get_formatted_name_2


class NamesTestCase(unittest.TestCase):
    """Тести для 'name_function_2.py'."""

    def test_first_last_name(self):
        """Чи працює з іменами на кшталт 'Janis Joplin'?"""
        formatted_name = get_formatted_name_2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Чи працює з іменами на кшталт 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name_2('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
