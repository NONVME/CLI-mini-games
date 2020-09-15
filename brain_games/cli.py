import prompt


def welcome_user():
    ''' prints a prompt for the entered value '''
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
