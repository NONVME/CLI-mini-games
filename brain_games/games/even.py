"""The module contains the basic rules and logic of the game."""

from random import randint

ISSUE_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def play():
    """Return the main logic of the game.

    Returns:
        game_question: equation description;
        game_answer: result of operation

    """
    number = randint(0, 100)
    is_even = number % 2 == 0
    if is_even:
        return number, 'yes'
    return number, 'no'
