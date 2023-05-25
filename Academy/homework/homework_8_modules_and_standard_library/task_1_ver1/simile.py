"""
This is a function that compares the strengths of things
for the rock-paper-scissors program.
"""


def compare(player_choice, computer_choice):
    """A function that generates the results of a duel."""
    dictionary_of_things = {'r': 0, 'p': 1, 's': 2}
    player_number = dictionary_of_things[player_choice]
    computer_number = dictionary_of_things[computer_choice]
    result_matrix = [
        [None, False, True],
        [True, None, False],
        [False, True, None]
    ]
    result = result_matrix[player_number][computer_number]
    return result
