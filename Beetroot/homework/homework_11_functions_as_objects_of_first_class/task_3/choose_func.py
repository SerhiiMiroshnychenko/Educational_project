# Write a function called 'choose_func' which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return
# the result of it. Otherwise, return the result of the second one.

"""def choose_func(nums: list, func1, func2):
    pass
# Assertions

def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]"""
def choose_func(nums: list, func1, func2):
    """A function for lists changing"""
    try:
        if min(nums) >= 0:
            return func1(nums)
        elif min(nums) < 0:
            return func2(nums)
    except TypeError as error:
        return f'Помічена помилка: {error.__class__}. Причина: {error}'

if __name__ == '__main__':
    def square_nums(nums): return [num ** 2 for num in nums]
    def remove_negatives(nums): return [num for num in nums if num > 0]

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    nums3 = [1, '2', 3, 4, 5]
    nums4 = [1, 2, 3.0, 4, .5]

    print(res1 := choose_func(nums1, square_nums, remove_negatives))
    print(res2 := choose_func(nums2, square_nums, remove_negatives))
    print(res3 := choose_func(nums3, square_nums, remove_negatives))
    print(res4 := choose_func(nums4, square_nums, remove_negatives))

