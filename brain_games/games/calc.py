"""The module contains the basic rules and logic of the game."""

from operator import add, mul, sub
from random import choice, randint

ISSUE_DESCRIPTION = 'What is the result of the expression?'


def play():
    """Return the main logic of the game.

    Returns:
        game_question: equation description;
        game_answer: result of operation

    """
    number1, number2 = [randint(0, 100) for _ in range(2)]
    operation = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    action = choice(list(operation))
    game_answer = operation[action](number1, number2)
    game_question = '{0} {1} {2}'.format(number1, action, number2)
    return game_question, game_answer
