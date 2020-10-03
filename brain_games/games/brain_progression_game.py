"""The module contains the basic rules and logic of the game."""

from itertools import islice
from random import randint

from prompt import integer


def play(name):
    """Print the main logic of the game.
    Args:
        name: the username in prompt.
    """
    counter = 0
    while counter < 3:
        counter += 1
        rand_step = randint(1, 10)
        rand_start = randint(0, 100)
        progression = list(islice((
            x + rand_start
            for x in range(100)
            if x % rand_step == 0), 10))
        rand_index = randint(0, 9)
        answer = progression[rand_index]
        progression[rand_index] = '..'
        print("Question: {}".format(' '.join(map(str, progression))))
        user_answer = integer("Your answer: ")
        if user_answer == answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(.",
                f"Correct answer was '{answer}'.\n",
                f"Let's try again, {name}!",
            )
            break
    else:

        print(f"Congratulations, {name}!")
