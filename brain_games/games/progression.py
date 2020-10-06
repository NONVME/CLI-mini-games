"""The module contains the basic rules and logic of the game."""

from itertools import islice
from random import randint

ISSUE_DESCRIPTION = 'What number is missing in the progression?'


def play():
    """Return the main logic of the game.

    Returns:
        game_question: equation description;
        game_answer: result of operation

    """
    step = randint(1, 10)
    start = randint(0, 100)
    progression = list(islice((
        x + start
        for x in range(100)
        if x % step == 0), 10))
    index = randint(0, 9)
    game_answer = progression[index]
    progression[index] = '..'
    game_question = '{0}'.format(' '.join(map(str, progression)))
    return game_question, game_answer
