"""The module contains the basic rules and logic of the game."""

import operator
from random import choice, randint

from prompt import integer


def play(name):
    """Print the main logic of the game.

    Args:
        name: the username in prompt.

    """
    counter = 0
    while counter < 3:
        counter += 1
        r_number1, r_number2 = [randint(0, 100) for _ in range(2)]
        action = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
        }
        r_action = choice(list(action))
        equation = action[r_action](r_number1, r_number2)
        print(f"Question: {r_number1} {r_action} {r_number2}")
        answer = integer("Your answer: ")
        if answer == equation:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{equation}'.\n",
                f"Let's try again, {name}!",
            )
            break
    else:
        print(f"Congratulations, {name}!")
