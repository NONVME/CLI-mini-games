"""The module contains the main logic for managing games."""

from prompt import string

QUANTITY_STEPS = 3


def play(game):
    """Return the logic of the requested game."""
    print('Welcome to the Brain Games!\n{0}\n'.format(game.DESCRIPTION))
    user_name = string('May I have your name? ')
    print('Hello, {0}!\n'.format(user_name))
    for _ in range(QUANTITY_STEPS):
        game_question, game_answer = game.generate_round()
        print('Question: {0}'.format(game_question))
        user_answer = string('Your answer: ')
        if user_answer != game_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answer, game_answer))
            print("Let's try again, {0}!".format(user_name))
            return
        print('Correct!')
    print('Congratulations, {0}'.format(user_name))
