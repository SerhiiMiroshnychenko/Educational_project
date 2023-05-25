# This feature simulates a rock-paper-scissors game

def rock_paper_scissors():
    """This function is a simulation of a rock-paper-scissors game."""
    from random import choice
    from simile import compare
    from game_result import get_game_result
    from the_rules_of_the_game import get_rules
    get_rules()
    things = ['r', 'p', 's']
    dictionary_of_choice = {'r': "ROCK", 'p': "PAPER", 's': "SCISSORS"}
    while True:
        player_choice = input("\nYour turn: ")
        computer_choice = choice(things)
        if player_choice == 'q':
            return print('\n\t\tGAME OVER.\nThank you for your attention.')
        elif player_choice in things:
            print(f"\nYour choice: \t {dictionary_of_choice[player_choice]}\t\t\t\t\t(Ваш вибір)")
            print(f"Computer choice: {dictionary_of_choice[computer_choice]}\t\t\t\t(Вибір компутера)")
            get_game_result(compare(player_choice, computer_choice))
        else:
            print("\nYou entered an invalid character.\t\t\t(Ви ввели неправильний символ)")
            print("Try again.\t\t\t\t\t\t\t\t\t(Спробуйте ще раз)")



        







