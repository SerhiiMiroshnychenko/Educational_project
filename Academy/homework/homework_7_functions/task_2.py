# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name
# and capital as parameters. Then create a dictionary from those two,
# with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary
# to make sure that it works as intended.

def make_country(country: str, capital: str) -> dict:
    """A function makes a dictionary with country's name and its capital"""
    return {country: capital, }


our_country = make_country('Ukraine', 'Kyiv')

print(our_country)


def show_country(country: str, capital: str) -> None:
    """A function makes and shows a dictionary with country's name and its capital"""
    print({country: capital, })


show_country('Poland', 'Warsaw')
