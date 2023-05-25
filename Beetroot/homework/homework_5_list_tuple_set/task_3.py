# Task 3 - Extracting numbers.
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list.
# Finally, print the list.
# Constraint: use only while loop for iteration


# Variant 1
def create_special_numbers():
    """The function that creates a list of special numbers"""
    numbers_1_100 = list(range(1, 101))
    counter = 0
    special_numbers = []

    while counter < len(numbers_1_100):
        if numbers_1_100[counter] % 7 == 0 and numbers_1_100[counter] % 5 != 0:
            special_numbers.append(numbers_1_100[counter])
        counter += 1
    return special_numbers


print(create_special_numbers())


# Variant 2
def generate_special_numbers():
    """The function that generates a list of special numbers"""
    return [x for x in range(1, 100) if x % 7 == 0 and x % 5 != 0]


print(generate_special_numbers())
