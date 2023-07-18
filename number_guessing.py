import random
import sys

INTRO = """(´• ω •`) ♡ WELCOME TO THE NUMBER GUESSING GAME! (´ε｀ )♡
You can guess a number from 1 to 10.
Guessing incorrectly will reduce your score.
Type 'quit' or 'q' to quit.
"""

def validate_input(guess):
    result = -1
    try:
        num = int(guess)
        result = num
    except ValueError:
        if guess in ['quit', 'q']:
            result = guess
    return result

def give_hint(score):
    score -= 10
    if GUESS > rand:
        print("HINT: The secret number is lower than your guess.")
    else:
        print("HINT: The secret number is greater than your guess.")
    return score

def check_result():
    if rand == GUESS:
        print(f"\nYou guessed the secret number: {rand}/100!")
        print(f"Your FINAL SCORE is {SCORE}!")
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
    SCORE = 100

    rand = random.randint(1, 10)

    while PLAYING:
        
        GUESS = validate_input(input("> "))
        if GUESS in ['quit', 'q']:
            print(f"\nThe secret number was {rand}!")
            exit_game()
        elif GUESS <= 0 or GUESS >= 11:
            print("\nPlease guess a number from 1 to 10.")
        else:
            PLAYING = check_result()
            SCORE = give_hint(SCORE)
