import sys
import wikipedia

# print(wikipedia.summary("BTS", auto_suggest=False, sentences=2))

INTRO = """(´• ω •`) ♡ WELCOME TO THE RANDOM WIKI PAGE GENERATOR! (´ε｀ )♡
This program will find a random wikipedia.
If you would like to read it, type 'yes'.
For a different article, type 'no'.
Type 'quit' to stop the program.
"""

print(INTRO)

while True:
    result = wikipedia.random()

    CHOICE = input(f"Would you like to read about {result}? ")
    if CHOICE == 'yes':
        page = wikipedia.page(result)
        print()
        print(page.title)
        print(page.content)
        print()

    elif CHOICE == 'quit':
        sys.exit()