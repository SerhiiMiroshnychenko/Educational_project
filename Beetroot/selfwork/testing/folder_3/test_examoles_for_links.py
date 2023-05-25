# https://docs.python-guide.org/writing/tests/

# UNITTEST
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

