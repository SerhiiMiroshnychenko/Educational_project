# Task 4 - The name check.
# Write a program that has a variable with your name stored (in lowercase)
# and then asks for your name as input. The program should check if your
# input is equal to the stored name even if the given name has another case,
# e.g., if your input is “Anton” and the stored name is “anton”, it should return True.

def name_checker(my_name: str):
    """The name check function"""
    if my_name.lower() == input('What is your name? Answer: ').lower():
        return True
    return False


print(name_checker('serhii'))
