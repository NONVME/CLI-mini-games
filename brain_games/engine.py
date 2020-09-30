"""The module contains the main logic for managing games."""

from prompt import string

from brain_games.games import brain_calc_game as calc_g
from brain_games.games import brain_even_game as even_g


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

    if name_of_the_game == 'brain_calc':
        return brain_calc

    elif name_of_the_game == 'brain_even':
        return brain_even
