import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тести для 'name_function.py'."""

    def test_first_last_name(self):
        """Чи працює з іменами на кшталт 'Janis Joplin'?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
