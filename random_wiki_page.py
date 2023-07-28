"""Random Wikipedia Page Generator
This script generates a random wiki page for the user, who can then
decide whether they would like to read it or not.
"""

import sys
import wikipedia

INTRO = """(´• ω •`) ♡ WELCOME TO THE RANDOM WIKI PAGE GENERATOR! (´ε｀ )♡
This program will find a random wikipedia.
If you would like to read it, type 'yes' or 'y'.
For a different article, type 'no'.
Type 'quit' or 'q' to stop the program.
"""

if __name__ == "__main__":
    print(INTRO)
    while True:
        result = wikipedia.random()
        CHOICE = input(f"Would you like to read about {result}? ")
        if CHOICE in ['yes', 'y']:
            page = wikipedia.page(result)
            print(f"\n{page.title}\n{page.content}\n")
        elif CHOICE == ['quit', 'q']:
            sys.exit()
