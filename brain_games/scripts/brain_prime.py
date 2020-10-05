"""Brain prime."""

from brain_games.engine import play, welcome_user
from brain_games.games import prime


def main():
    """Call the main logic of the game."""
    welcome_user(prime)
    play(prime)


if __name__ == '__main__':
    main()
