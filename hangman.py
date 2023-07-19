import random
import sys

# hangman ascii art and word bank taken from https://github.com/chrishorton
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def check_guess(guess, start):
    if guess == secret:
        for i in range(len(location)):
            location[i] = True
    else:
        for _ in range(len(secret)):
            j = secret.find(guess, start)
            if j != -1:
                start = j + 1
                location[j] = True
    print_results()

def check_attempts(guess):
    print(f"{guess} is NOT a letter.")
    print_results()
    if ATTEMPTS >= 6:
        print("You have run out of attempts!")
        print(f"The secret word was {secret}!\n")
        sys.exit()

def print_results():
    print(HANGMANPICS[ATTEMPTS])
    for num, value in enumerate(location):
        if value:
            print(secret[num], end=" ")
        else:
            print("_", end=" ")
    print("\n")
    if GUESS not in guessed:
        guessed.append(GUESS)

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

INTRO = """(´• ω •`) ♡ WELCOME TO ANIMAL HANGMAN! (´ε｀ )♡
When you see the ">" symbol, type a letter to guess!"""

while True:
    print(INTRO)
    secret = random.choice(words)
    ATTEMPTS = 0
    location = []
    for _ in range(len(secret)):
        location.append(False)

    guessed = []
    GUESS = ""

    print_results()
    GUESS = input("> ")

    PLAYING = True
    while PLAYING:
        START = 0
        if GUESS == secret:
            check_guess(GUESS, START)
        elif GUESS in guessed:
            print("You have already guessed this letter.\n")
        elif secret.find(GUESS) == -1:
            ATTEMPTS += 1
            check_attempts(GUESS)
        else:
            check_guess(GUESS, START)

        if all(location):
            print(f"YOU WON! You correctly guessed the secret word: {secret}!")
            sys.exit()
        else:
            GUESS = input("> ")
    sys.exit()
