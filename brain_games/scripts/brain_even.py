"""Brain_even."""

from brain_games import engine


def main():
    """Call the main logic of the game."""
    print(
        f"Welcome to the Brain Games!\n",
        f"Answer \"yes\" if number even otherwise answer \"no\".\n",
    )
    engine.welcome_user()
    engine.play()


if __name__ == '__main__':
    main()
