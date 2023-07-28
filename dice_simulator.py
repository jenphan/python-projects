"""Dice Simulator
This script allows the user to roll a dice multiple times. The statistics
of dice rolls will automatically printed upon exiting the script.
"""

import random
import sys

INTRO = """(´• ω •`) ♡ WELCOME TO THE DICE ROLLING SIMULATOR! (´ε｀ )♡
When prompted, type 'yes' or 'y' to roll.
Type 'stats' or 's' to view your roll statistics.
Type 'no' or 'n' to stop the program.
"""


class Dice():
    """A class used to represent a dice"""
    def __init__(self):
        """Constructs all the necessary attributes for the dice object"""
        self.dice = [1, 2, 3, 4, 5, 6]
        self.stats = [0] * 6
        self.total = 0

    def roll(self):
        """Generates and prints a number from 1 to 6"""
        value = random.choice(self.dice)
        self.stats[value - 1] += 1
        self.total += 1
        print(f"> You rolled a {value}. (♡˙︶˙♡)")

    def statistics(self):
        """Prints amount of times a side of the dice is rolled"""
        for side in self.dice:
            print(f"> {side}'s Rolled: {self.stats[side - 1]}/{self.total}")
        print()


if __name__ == "__main__":
    print(INTRO)
    user = Dice()
    while True:
        INPUT = input("\nRoll the dice? ")
        if INPUT in ["yes", "y"]:
            user.roll()
        elif INPUT in ["stats", "s", "no", "n"]:
            user.statistics()
            if INPUT in ["no", "n"]:
                print("\n｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡Thank you for playing!")
                sys.exit()
        else:
            print("Please select a valid option.")
