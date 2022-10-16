import unittest
from name_function_2 import get_formatted_name_2


class NamesTestCase(unittest.TestCase):
    """Тести для 'name_function_2.py'."""

    def test_first_last_name(self):
        """Чи працює з іменами на кшталт 'Janis Joplin'?"""
        formatted_name = get_formatted_name_2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
