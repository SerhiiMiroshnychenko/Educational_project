# Task 1
# Pick your solution to one of the exercises in this module.
# Design tests for this solution and write tests using unittest library.
import unittest
from unittest import TestCase
from ...homework_13_classes.task_2.task_2 import Dog

class TestDog(TestCase):
    def setUp(self) -> None:
        self.test_dog = Dog('jon', 3)
    def test_human_age(self):
        self.assertEqual(self.test_dog.human_age(), 21)

    def test_dog_name(self):
        self.assertEqual(self.test_dog.dog_name, 'Jon')

    def test_change_age(self):
        self.assertEqual(self.test_dog.dog_age, 3)
        self.test_dog.dog_age = 4
        self.assertEqual(self.test_dog.dog_age, 4)
        self.assertEqual(self.test_dog.human_age(), 28)

if __name__ == '__main__':
    unittest.main()
