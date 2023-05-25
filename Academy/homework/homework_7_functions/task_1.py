# Task 1
# A simple function.
# Create a simple function called favorite_movie,
# which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.

def favorite_movie(name: str) -> None:
    """A function shows favorite movie's name"""
    print(f'My favorite movie is named "{name}".')


favorite_movie('The Lord of the Rings')
