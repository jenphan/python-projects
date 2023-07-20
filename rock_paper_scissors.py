import sys
import random

CHOICES = ['rock', 'paper', 'scissors']
SCORE = [0, 0, 0]

def determine_winner(comp, user):
    result = 1
    if user == comp:
        result = -1
    elif (comp > user) or (user == 2 and comp == 0):
        result = 0
    return result

def print_winner(result, comp, score):
    print(f"The computer picked: {comp}.")
    match result:
        case -1:
            score[2] += 1
            print("YOU TIED!")
        case 0:
            score[1] += 1
            print("YOU LOSE!")
        case 1:
            score[0] += 1
            print("YOU WIN!")
    return score

def print_score(score):
    print(f"\nWINS: {score[0]}")
    print(f"LOSSES: {score[1]}")
    print(f"TIES: {score[2]}\n")

INTRO = """(´• ω •`) ♡ WELCOME TO ROCK PAPER SCISSORS! (´ε｀ )♡
Type 'rock', 'paper', or 'scissors' to play.
Type 'quit' to stop playing."""

print(INTRO)

while True:
    COMPUTER = random.choice(CHOICES)
    USER = input("\n> ")
    if USER == 'quit':
        print_score(SCORE)
        sys.exit()
    if USER not in CHOICES:
        print("Please enter a valid move.")
    else:
        COMPID = CHOICES.index(COMPUTER)
        USERID = CHOICES.index(USER)
        RESULT= determine_winner(COMPID, USERID)
        SCORE = print_winner(RESULT, COMPUTER, SCORE)
