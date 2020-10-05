"""Brain calc."""

from brain_games.engine import play, welcome_user
from brain_games.games import calc


def main():
    """Call the main logic of the game."""
    welcome_user(calc)
    play(calc)


if __name__ == '__main__':
    main()
