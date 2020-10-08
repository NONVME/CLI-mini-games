"""The module contains the basic rules and logic of the game."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'
STEP_MIN = 1
STEP_MAX = 10
START_MIN = 0
START_MAX = 100
LENGTH = 10


def generate_round():
    """Return the main logic of the game."""
    step = randint(STEP_MIN, STEP_MAX)
    start = randint(START_MIN, START_MAX)
    progression = [(start + (i * step)) for i in range(LENGTH)]
    index = randint(0, LENGTH - 1)
    game_answer = str(progression[index])
    progression[index] = '..'
    game_question = ' '.join(map(str, progression))
    return game_question, game_answer
