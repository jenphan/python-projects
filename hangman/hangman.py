"""Hangman Game

This script allows the user to play a game of hangman.
"""

import random
import sys
import hm_info

# hangman ascii art and word bank taken from https://github.com/chrishorton
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

class Hangman():
    """A class used to represent a game of hangman"""
    def __init__(self):
        """Constructs all the necessary attributes for the hangman object."""
        self.secret = random.choice(hm_info.WORDS)
        self.attempts = 0
        self.blanks = []
        self.history = []
        for _ in range(len(self.secret)):
            self.blanks.append(False)
    def check_guess(self, guess, start):
        """Sets true if guessed letter appears in the secret word."""
        if guess == self.secret:
            for num, value in enumerate(self.blanks):
                value[num] = True
        else:
            for _ in range(len(self.secret)):
                i = self.secret.find(guess, start)
                if i != -1:
                    start = i + 1
                    self.blanks[i] = True
        self.print_results()
        self.history.append(GUESS)
    def incorrect_guess(self, guess):
        """Checks whether maximum incorrect guesses (6) has been reachde"""
        self.attempts += 1
        print(f"{guess} is NOT a letter.")
        self.print_results()
        if self.attempts >= 6:
            print("You have run out of attempts!")
            print(f"The secret word was {self.secret}!\n")
            sys.exit()
    def print_results(self):
        """Print a hangman visual"""
        print(hm_info.HANGMAN[self.attempts])
        print("\n")
        for num, value in enumerate(self.blanks):
            if value:
                print(self.secret[num], end=" ")
            else:
                print("_", end=" ")
        print("\n")

if __name__ == "__main__":
    print(hm_info.INTRO)
    user = Hangman()
    user.print_results()
    GUESS = input("> ")
    while True:
        START = 0
        if GUESS in user.history:
            print("You have already guessed this letter.\n")
        elif not GUESS.isalpha():
            print("Please enter a valid letter.\n")
        elif user.secret.find(GUESS) == -1:
            user.incorrect_guess(GUESS)
        else:
            user.check_guess(GUESS, START)

        if all(user.blanks):
            print(f"YOU WON! You correctly guessed the secret word: {user.secret}!")
            sys.exit()
        else:
            GUESS = input("> ")
