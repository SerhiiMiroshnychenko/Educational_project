import unittest
from unittest import TestCase

import examples


class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
        self.test_person = examples.Person('Jon', 'man', 35, 175.0, 75)

    def test_love(self):
        self.assertEqual(self.test_person.love_time, 0)
        self.test_person.love('Lisa')
        self.assertEqual(self.test_person.love_time, 1)

        # self.love_time += 1
        # print(f'I love {honey_name.capitalize()}!
        # I am {self.love_time} time in love!')


class TestDog(TestCase):
    def setUp(self) -> None:
        self.test_dog = examples.Dog('jon', 3)
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
