import sys

"""
hangman ascii art taken from https://github.com/chrishorton
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
"""

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

INTRO = """(´• ω •`) ♡ WELCOME TO HANGMAN! (´ε｀ )♡
When you see the ">" symbol, type a letter to guess!
"""

while True:
    print(INTRO)
    secret = "apple"
    location = []
    guess = input("> ")
    guessed = []
    PLAYING = True;
    attempts = 0

    for i in range(len(secret)):
        location.append(False)

    solved = False

    while PLAYING:
        start = 0
        if guess in guessed:
            print("You have already guessed this letter.\n")
        elif secret.find(guess) == -1:
            attempts += 1
            print("-1 attempt")
            print(HANGMANPICS[attempts])
            for x in range(len(location)):
                if location[x]:
                    print(secret[x], end=" ")
                else:
                    print("_", end=" ")
            print("\n")
            if attempts >= 6:
                print(HANGMANPICS[attempts])
                print("You have run out of attempts!")
                print(f"The secret word was {secret}!\n")
                sys.exit()
        else:
            for _ in range(len(secret)):
                j = secret.find(guess, start)
                if j != -1:
                    start = j + 1
                    location[j] = True
            
            print(HANGMANPICS[attempts])
            for x in range(len(location)):
                if location[x]:
                    print(secret[x], end=" ")
                else:
                    print("_", end=" ")
            print("\n")
        
        guessed.append(guess)

        if all(location):
            print("\nSOLVED")
            sys.exit()
        else:
            guess = input("> ")
    sys.exit()
