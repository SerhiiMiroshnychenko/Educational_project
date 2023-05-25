"""
This is a function that outputs the results of the game
for the rock-paper-scissors program
"""


def get_game_result(compare_result):
    """A function that outputs the results of a duel."""
    print("\n\t\t\t\t\tRESULT:")
    if compare_result:
        print("\nCongratulations!!!\t\t\t(Вітаю!!!)")
        print("WINNING!!!\t\t\t\t\t(ПЕРЕМОГА!!!)")
    elif compare_result is None:
        print("\nNONE\t\t\t\t\t\t(НІЧИЯ)")
    else:
        print("\nLoss...\t\t\t\t\t\t(Програш...)")
        print("Good luck next time!\t\t(Щасти наступного разу!)")
