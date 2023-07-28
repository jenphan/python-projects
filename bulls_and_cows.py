"""Bulls and Cows
This script allows the user to guess a four digit number with
bulls (right position) and cows (wrong positions)."""


import random
import sys

INTRO = """(´• ω •`) ♡ WELCOME TO BULLS AND COWS! (´ε｀ )♡
The objective is to guess a four digit secret number.
For every guess, you will be given BULLS and COWS.
BULLS are the correct digits in the correct places.
COWS are the correct digits in the wrong places.
"""


class Game():
    """A class to represent a game of bulls and cows"""
    def __init__(self):
        digits = list(range(10))
        random.shuffle(digits)
        self.secret = "".join(map(str, digits[:4]))
        self.solved = False
        self.bulls = 0
        self.cows = 0

    def get_results(self, guess):
        """Checks bulls and cows for user's guess"""
        self.bulls = 0
        self.cows = 0
        for i in range(4):
            if self.secret[i] == guess[i]:
                self.bulls += 1
            elif guess[i] in self.secret:
                self.cows += 1
        if self.bulls == 4:
            self.solved = True

    def print_results(self):
        """Generate and print the bulls and cows amount"""
        print(f"{self.bulls} Bull(s)\t{self.cows} Cow(s)\n")


def validate_guess(guess):
    """Validate that guess is four digits and non-repeating"""
    result = False
    if len(guess) == 4:
        if len(set(guess)) == len(guess):
            result = True
    return result


if __name__ == "__main__":
    print(INTRO)
    user = Game()
    print("Please enter your guess.\n")
    while True:
        GUESS = input("> ")
        if validate_guess(GUESS):
            user.get_results(GUESS)
            if user.solved:
                print(f"You are correct! The secret number was {user.secret}.")
                sys.exit()
            else:
                user.print_results()
        else:
            if len(GUESS) == 4:
                print("Your guess should not include duplicates.")
            else:
                print("Your guess should be a length of 4.")
