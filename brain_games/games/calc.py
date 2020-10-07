"""The module contains the basic rules and logic of the game."""

from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    """Return the main logic of the game."""
    number1, number2 = [randint(0, 100) for _ in range(2)]
    operation = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    action = choice(list(operation))
    game_answer = str(operation[action](number1, number2))
    game_question = '{0} {1} {2}'.format(number1, action, number2)
    return game_question, game_answer
