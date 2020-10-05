"""Brain even."""

from brain_games.engine import play, welcome_user
from brain_games.games import even


def main():
    """Call the main logic of the game."""
    welcome_user(even)
    play(even)


if __name__ == '__main__':
    main()
