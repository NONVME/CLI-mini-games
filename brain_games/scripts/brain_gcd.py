"""Brain gcd."""

from brain_games.engine import play, welcome_user
from brain_games.games import gcd


def main():
    """Call the main logic of the game."""
    welcome_user(gcd)
    play(gcd)


if __name__ == '__main__':
    main()
