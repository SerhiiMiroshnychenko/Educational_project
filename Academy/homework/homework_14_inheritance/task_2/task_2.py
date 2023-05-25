# Task 2
# Mathematician
# Implement a class Mathematician which is a helper class
# for doing math operations on lists
# The class doesn't take any attributes and only has methods:
"""square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
```
class Mathematician:
    pass

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]"""

class Mathematician:

    @staticmethod
    def square_nums(array: list[int]) -> list[int]:
        """Takes a list of integers and returns the list of squares"""
        return [x*x for x in array]

    @staticmethod
    def remove_positives(array: list[int]) -> list[int]:
        """Takes a list of integers and returns it without positive numbers"""
        return [x for x in array if x < 0]

    @staticmethod
    def filter_leaps(array: list[int]) -> list[int]:
        """Takes a list of integers and removes those that are not 'leap years'"""
        return [x for x in array if x % 4 == 0]

if __name__ == '__main__':
    m = Mathematician()
    print(m.square_nums([7, 11, 5, 4]))
    print(m.remove_positives([26, -11, -8, 13, -90]))
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))