"""Brain_calc."""

from brain_games import engine


def main():
    """Call the main logic of the game."""
    print(
        'Welcome to the Brain Games!\n',
        'Answer \"yes\" if number even otherwise answer \"no\".\n',
    )
    engine.welcome_user()
    engine.play('brain_calc')()


if __name__ == '__main__':
    main()
