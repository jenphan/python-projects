import random
import sys

INTRO = """(´• ω •`) ♡ WELCOME TO THE NUMBER GUESSING GAME! (´ε｀ )♡
You can guess a number from 1 to 10.
Type 'hint' or 'h' for a hint.
Type 'quit' or 'q' to quit.
"""

def validate_input(userinput):
    result = -1
    try:
        num = int(userinput)
        result = num
    except ValueError:
        if userinput in ['quit', 'q', 'hint', 'h']:
            result = userinput;
    return result

def check_result(actual, guess):
    if actual == guess:
        print(f"\nYou guessed the secret number! {rand}")
        print("Would you like to play again? (y/n)")
        again = input("> ")
        if again not in ['yes', 'y']:
            exit_game()
        return False
    print("\nYou did not guess the number! Guess again!")
    return True

def exit_game():
    print("\nThank you for playing!")
    sys.exit()

while True:
    print(INTRO)
    PLAYING = True
    GUESS = ""
    rand = random.randint(1, 10)

    while PLAYING:
        GUESS = validate_input(input("> "))
        if GUESS in ['quit', 'q']:
            print(f"\nThe secret number was {rand}!")
            exit_game()
        elif GUESS in ['hint', 'h']:
            print("Hint!")
        elif GUESS <= 0 or GUESS >= 11:
            print("\nPlease guess a number from 1 to 10.")
        else:
            PLAYING = check_result(rand, GUESS)
