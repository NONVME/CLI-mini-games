"""The module contains the basic rules and logic of the game."""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def generate_round():
    """Return the main logic of the game."""
    number = randint(0, 100)
    is_even = number % 2 == 0
    if is_even:
        return number, 'yes'
    return number, 'no'
