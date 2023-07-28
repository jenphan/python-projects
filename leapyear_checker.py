"""Leap Year Checker
This script returns whether the user inputted year is a leap year or not.
"""

import sys

INTRO = """(´• ω •`) ♡ WELCOME TO THE LEAP YEAR CHECKER! (´ε｀ )♡
Type a year to check whether it is a leap year or not.
Type 'quit' or 'q' to stop the program.
"""


def check_leapyear(year):
    """Checks whether year given is a leap year"""
    leapyear = False
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 == 0):
            leapyear = True
        elif year % 100 != 0:
            leapyear = True
    if leapyear:
        print(f"{year} is a leap year.\n")
    else:
        print(f"{year} is NOT a leap year.\n")


def validate_year(year):
    """Checks whether user input is a valid year"""
    if year.isdecimal():
        check_leapyear(int(year))
    else:
        print("Please use a valid numeric year.\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            YEAR = arg
            validate_year(YEAR)
        sys.exit()
    else:
        print(INTRO)
        while True:
            YEAR = input("> ")
            if YEAR in ['quit', 'q']:
                sys.exit()
            else:
                validate_year(YEAR)
