"""The module contains the basic rules and logic of the game."""

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
        r_number1, r_number2 = [randint(0, 100) for _ in range(2)]
        for i in range(min(r_number1, r_number2), 0, -1):
            if r_number1 % i == 0 and r_number2 % i == 0:
                answer = i
                break
        print(f"Question: {r_number1} {r_number2}")
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
