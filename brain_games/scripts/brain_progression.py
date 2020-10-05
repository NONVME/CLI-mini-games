"""Brain progression."""

from brain_games.engine import play, welcome_user
from brain_games.games import progression


def main():
    """Call the main logic of the game."""
    welcome_user(progression)
    play(progression)


if __name__ == '__main__':
    main()
