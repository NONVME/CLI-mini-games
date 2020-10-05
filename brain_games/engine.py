"""The module contains the main logic for managing games."""

from prompt import string

QUANTITY_STEPS = 3


def welcome_user(game):
    """Print a prompt for the enter value.

    Args:
        game: the name of the game.

    """
    global user_name
    print('Welcome to the Brain Games!\n{0}\n'.format(game.ISSUE_DESCRIPTION))
    user_name = string('May I have your name? ')
    print('Hello, {0}!\n'.format(user_name))


def play(game):
    """Return the logic of the requested game.

    Args:
        game: the name of the game.

    Returns:
        None

    """
    for step in range(QUANTITY_STEPS):
        game_question, game_answer = game.play()
        user_answer = string(
            'Question: {0}\nYour answer: '.format(game_question)
        )
        if user_answer != str(game_answer):
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answer, game_answer)
            )
            print("Let's try again, {0}!".format(user_name))
            return
        print('Correct!')
    print('Congratulations, {0}'.format(user_name))
