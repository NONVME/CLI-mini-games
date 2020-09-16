"""Command line interface."""

import prompt


def welcome_user():
    """Print a prompt for the enter value."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
