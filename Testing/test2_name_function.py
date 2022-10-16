import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Тести для 'name_function.py'."""

    def test_first_name(self):
        """Чи працює з іменами на кшталт 'Janis'?"""
        formatted_name = get_formatted_name('janis', True)
        self.assertEqual(formatted_name, 'Janis True')


if __name__ == '__main__':
    unittest.main()
