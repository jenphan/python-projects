"""Fibonnaci Checker
This script allows the user to check whether
a number is part of the fibonacci sequence.
"""

import math
import sys

INTRO = """(´• ω •`) ♡ WELCOME TO THE FIBONACCI CHECKER! (´ε｀ )♡
Type a number to check whether it is part of the fibonnaci sequence.
Type 'quit' or 'q' to stop the program.
"""


def is_perfect_square(num):
    """Subfunction – checks whether a number is a perfect square"""
    root = int(math.sqrt(num))
    return root * root == num


def is_fibonacci(num):
    """Prints whether a number is part of the fibonacci sequence"""
    if (is_perfect_square(5 * num * num * 4)
            or is_perfect_square(5 * num * num - 4)):
        print(f"{NUM} is a fibonacci number.")
    else:
        print(f"{NUM} is NOT a fibonacci number.")


def validate_num(num):
    """Checks whether user input contains only decimal numbers"""
    if num.isdecimal():
        is_fibonacci(int(num))
    else:
        print("Please use a valid number.\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            NUM = arg
            validate_num(NUM)
        sys.exit()
    else:
        print(INTRO)
        while True:
            NUM = input("> ")
            if NUM in ["quit", "q"]:
                sys.exit()
            else:
                validate_num(NUM)
                print()
