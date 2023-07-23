"""Dice Simulator

This script allows the user to roll a dice multiple times. The statistics of dice rolls will
automatically printed upon exiting the script.
"""

import random
import sys

dice = [1, 2, 3, 4, 5, 6]
history = []

def intro_msg():
    print("(´• ω •`) ♡ WELCOME TO THE DICE ROLLING SIMULATOR! (´ε｀ )♡")
    print("type 'yes' or 'y' to roll.")

def roll_dice():
    roll = random.choice(dice)
    history.append(roll)
    print(f"> You rolled a {roll}. (♡˙︶˙♡)")

def statistics(rolled):
    stats  = [0] * 6

    for num in rolled:
        stats[num - 1] += 1

    total = sum(stats)

    print("\n｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡Thank you for playing!")
    for side in dice:
        print(f"> {side}'s Rolled: {stats[side - 1]}/{total}")

intro_msg()

while True:
    PLAYING = input("\nRoll the dice? ")

    if PLAYING in ["yes", "y"]:
        roll_dice()
    else:
        statistics(history)
        sys.exit()
