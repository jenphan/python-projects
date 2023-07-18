import random
import sys

INTRO = """(´• ω •`) ♡ WELCOME TO THE NUMBER GUESSING GAME! (´ε｀ )♡
You can guess a number from 1 to 10.
Type 'hint' or 'h' for a hint.
"""

def validate_input(input):
    try:
        num = int(input)
        return num
    except ValueError:
        return -1

def check_win(actual, user):
    if (actual == user):
        return True
    else:
        return False

while True:
    print(INTRO)
    rand = random.randint(1, 10)
    guess = validate_input(input("> "))

    if guess <= 0 or guess >= 11:
        print("Please guess a number from 1 to 10.")
    else:
        if check_win(rand, guess):
            print(f"You guessed the secret number!, {rand}")
        else:
            print(f"You did not guess the number!, {rand}")
    sys.exit()