# Create a function that takes on an input random ints (between 1 and 10) and returns the list,
# without duplicates. Try to create two versions of this function - first with usage set and list
# constructors and second only using for-in loops.

# Загальна ідея функція яка приймає наперед невідому к-сть параметрів числових, повертає список без дублікатів
# Варіант 1. За допомогою set()
# Варіант 2. За допомогою циклу for-in loops
# *agrs & len(args)

def no_duplicates(*args):
    """Without duplicates"""
    result = []
    for i in range(len(args)):
        if i not in result:
            result.append(i)
    return result


print(no_duplicates(1, 2, 3, 3, 3, 4, 5, 6, 7, 7))
