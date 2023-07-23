"""Countdown Timer

This script allows the user to set a countdown timer for a specified amount of minutes and seconds.

This file contains:
    * main - main function
"""

import time

INTRO = """(´• ω •`) ♡ WELCOME TO COUNTDOWN TIMER! (´ε｀ )♡
When prompted, type how many minutes and seconds you
would like to set the countdown timer for.
"""

def main(minutes, seconds):
    """Gets user input and creates text-based timer

    Args:
        minutes (int): The amount of minutes
        seconds (int): The amount of seconds

    Returns:
        none
    """
    print()
    total_secs = (minutes * 60) + seconds
    while total_secs:
        mins = total_secs // 60
        secs = total_secs % 60
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        total_secs -= 1
    print("TIMER IS UP!")

if __name__ == "__main__":
    print(INTRO)
    MINUTES = int(input("Enter minutes: "))
    SECONDS = int(input("Enter seconds: "))
    main(MINUTES, SECONDS)
