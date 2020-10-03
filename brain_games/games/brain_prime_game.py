"""The module contains the basic rules and logic of the game."""

from itertools import islice
from random import randint

from prompt import string


def play(name):
    """Print the main logic of the game.

    Args:
        name: the username in prompt.

    """
    counter = 0
    while counter < 3:
        counter += 1
        global rand_n
        rand_n = randint(0, 100)
        print("Question: {} is prime?".format(rand_n))
        user_answer = string("Your answer: ")
        if user_answer == answer():
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(.",
                f"Correct answer was '{answer()}'.\n",
                f"Let's try again, {name}!",
            )
            break
    else:

        print(f"Congratulations, {name}!")


def is_Prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def answer():
    if is_Prime(rand_n):
        return 'yes'
    return 'no'
