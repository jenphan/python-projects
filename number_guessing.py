"""Number Guessing Game
This script allows the user to guess a secret number from 1 to 10.
"""

import random
import sys

INTRO = """(´• ω •`) ♡ WELCOME TO THE NUMBER GUESSING GAME! (´ε｀ )♡
You can guess a number from 1 to 10.
Guessing incorrectly will reduce your score.
Type 'quit' or 'q' to quit.
"""


class Game():
    """A class used to represent a guessing game"""
    def __init__(self):
        """Constructs all necessary attributes for the guessing game object."""
        self.secret = random.randint(1, 10)
        self.score = 100
        self.guess = ""

    def validate_guess(self, guess):
        """Checks guess is either valid number or quit"""
        if self.score <= 0:
            self.lose_game()
        else:
            try:
                self.guess = int(guess)
                return True
            except ValueError:
                if guess in ['quit', 'q']:
                    self.quit_game()
        return False

    def set_guess(self, guess):
        """Sets the value for guess"""
        self.guess = guess

    def check_result(self):
        """Checks whether the guess is correct"""
        if self.secret == self.guess:
            print(f"\nYOU WIN! You guessed the secret number: {self.secret}!")
            print(f"Your FINAL SCORE is {self.score}/100!")
            sys.exit()
        if self.guess <= 0 or self.guess >= 11:
            print("\nPlease guess a number from 1 to 10.")
        else:
            print("\nYou did not guess the number! Guess again!")
            user.give_hint()

    def give_hint(self):
        """Generate and print a hint for incorrect answers"""
        self.score -= 10
        if user.guess > user.secret:
            print("HINT: The secret number is lower than your guess.")
        else:
            print("HINT: The secret number is greater than your guess.")

    def lose_game(self):
        """Print the lose game message"""
        print("\nYOU LOSE! Your final score has reached 0!")
        print(f"The secret number was {self.secret}!")
        sys.exit()

    def quit_game(self):
        """Print and exit the game"""
        print("\nThank you for playing!")
        sys.exit()


if __name__ == "__main__":
    print(INTRO)
    user = Game()

    while True:
        VALID = user.validate_guess(input("> "))
        if VALID:
            user.check_result()
        else:
            print("\nPlease guess a number from 1 to 10.")
