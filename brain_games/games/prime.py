"""The module contains the basic rules and logic of the game."""

from random import randint

ISSUE_DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def play():
    """Return the main logic of the game.

    Returns:
        game_question: equation description;
        game_answer: result of operation

    """
    number = randint(0, 100)
    game_question = '{0} is prime?'.format(number)
    if is_prime(number):
        return game_question, 'yes'
    return game_question, 'no'


def is_prime(n):
    """Return True if number is prime."""
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
