"""The module contains the basic rules and logic of the game."""

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
        r_number = randint(0, 100)
        print(f"Question: {r_number}")
        answer = string("Your answer: ")
        even = r_number % 2 == 0
        if answer == "yes" and even:
            print("Correct!")
        elif answer == "no" and not even:
            print("Correct!")
        else:
            correct_answer = "yes" if answer == "no" else "no"
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct_answer}'.\n",
                f"Let's try again, {name}!",
            )
            break
    else:
        print(f"Congratulations, {name}!")
