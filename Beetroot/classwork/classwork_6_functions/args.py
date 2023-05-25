def no_duplicates(*args):
    """Without duplicates"""
    return list(set(args))


print(no_duplicates(1, 2, 3, 3, 3, 4, 5, 6, 7, 7))
