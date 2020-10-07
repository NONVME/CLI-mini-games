"""The module contains the basic rules and logic of the game."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    """Return the main logic of the game.

    Returns:
        game_question: equation description;
        game_answer: result of operation

    """
    number1, number2 = [randint(0, 100) for _ in range(2)]
    game_question = '{0} {1}'.format(number1, number2)
    game_answer = str(gcd(number1, number2))
    return game_question, game_answer


def gcd(a, b):
    """Return the gcd of numbers."""
    while b:
        a, b = b, a % b
    return a
