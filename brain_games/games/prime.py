"""The module contains the basic rules and logic of the game."""

from math import sqrt
from random import randint

DESCRIPTION = ('Answer "yes" if given number is prime. Otherwise answer "no".')
MIN_PRIME = 2


def generate_round():
    """Return the main logic of the game."""
    number = randint(MIN_PRIME, 100)
    game_question = '{0} is prime?'.format(number)
    game_answer = 'yes' if is_prime(number) else 'no'
    return game_question, game_answer


def is_prime(n):
    """Return True if number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True
