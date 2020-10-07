"""Brain prime."""

from brain_games.engine import generate_round
from brain_games.games import prime


def main():
    """Call the main logic of the game."""
    generate_round(prime)


if __name__ == '__main__':
    main()
