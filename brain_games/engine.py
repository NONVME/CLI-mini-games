"""The module contains the main logic for managing games."""

from prompt import string

from brain_games.games import brain_calc_game as calc_g
from brain_games.games import brain_even_game as even_g
from brain_games.games import brain_gcd_game as gcd_g
from brain_games.games import brain_progression_game as progression_g
from brain_games.games import brain_prime_game as prime_g


def welcome_user():
    """Print a prompt for the enter value."""
    global name
    name = string("May I have your name? ")
    print(f"Hello, {name}!\n")


def play(name_of_the_game):
    """Return the logic of the requested game.

    Args:
        name_of_the_game: the name of the game.

    Returns:
        func

    """

    def brain_even():
        even_g.play(name)

    def brain_calc():
        calc_g.play(name)

    def brain_gcd():
        gcd_g.play(name)

    def brain_progression():
        progression_g.play(name)

    def brain_prime():
        prime_g.play(name)

    if name_of_the_game == 'brain_calc':
        return brain_calc

    if name_of_the_game == 'brain_even':
        return brain_even

    if name_of_the_game == 'brain_gcd':
        return brain_gcd

    if name_of_the_game == 'brain_progression':
        return brain_progression

    if name_of_the_game == 'brain_prime':
        return brain_prime
