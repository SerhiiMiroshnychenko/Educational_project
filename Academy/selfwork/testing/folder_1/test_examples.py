import unittest
import examples

class TestExamples(unittest.TestCase):

    def test_full_names(self):
        full1 = examples.full_name('boris', 'johnson')
        self.assertEqual(full1, 'Boris Johnson', msg='It is wrong.')
        full2 = examples.full_name('bOris', 'JOHNSON')
        self.assertEqual(full2, 'Boris Johnson', msg='It is wrong.')

class TestSquares(unittest.TestCase):

    def test_squares(self):
        square = examples.squares([1, 2, 3, 4])
        self.assertEqual(square, [1, 4, 9, 16], msg='It is wrong.')

