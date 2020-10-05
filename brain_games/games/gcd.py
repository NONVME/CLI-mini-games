"""The module contains the basic rules and logic of the game."""

from random import randint

ISSUE_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def play():
    """Return the main logic of the game.

    Returns:
        game_question: equation description;
        game_answer: result of operation

    """
    number1, number2 = [randint(0, 100) for _ in range(2)]
    for i in range(min(number1, number2), 0, -1):
        if number1 % i == 0 and number2 % i == 0:
            game_answer = i
            break
    game_question = '{0} {1}'.format(number1, number2)
    return game_question, game_answer
