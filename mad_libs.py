"""Madlibs Generator
This script allows the user to play a game of madlibs.
"""
import sys

INTRO = """(´• ω •`) ♡ WELCOME TO THE MADLIBS GENERATOR! (´ε｀ )♡
Follow the prompts and you will get your madlib.
"""

adj = []
noun = []
verb = []
time = []
adv = []
interj = []
animal = []
food = []
loc = []
game = []
name = []
color = []
body = []


def madlib1_input():
    """Get words for Madlibs 1"""
    print("Please type 5 adjectives (seperated by enter)")
    for _ in range(5):
        adj.append(input("> "))

    print("\nPlease enter 4 plural nouns (seperated by enter)")
    for _ in range(4):
        noun.append(input("> "))

    print("\nPlease enter 2 nouns (seperated by enter)")
    for _ in range(2):
        noun.append(input("> "))

    print("\nPlease enter 6 verbs (seperated by enter)")
    for _ in range(6):
        verb.append(input("> "))

    time.append(input("\nPlease enter a time of day\n> "))
    adv.append(input("\nPlease enter an adverb\n> "))
    interj.append(input("\nPlease enter an interjection\n> "))


def madlib1():
    """Generate and print Madlibs 1"""
    madlib1_input()
    print("\nVALENTINE'S DAY MADLIB")
    print(f"I have a {adj[0]} admirer.")
    print(f"My admirer leaves {noun[0]} and {noun[1]} in the mailbox.")
    print(f"The letters say \"You are my {adj[1]} {noun[4]}.", end=" ")
    print(f"I want to {verb[0]}. Please be mine.\n")
    print("Sometimes, my admirer leaves me chocolate with", end=" ")
    print(f" little {noun[2]} on top.")
    print(f"It makes me want to {verb[1]}.\n")
    print("I finally decided to find out who my admirer is.")
    print(f"Yesterday {time[0]}, I hid in the {noun[3]} by the mailbox.")
    print(f"I {verb[2]} for hours! Nobody came by.")
    print(f"The sky turned {adj[2]} and {adj[3]}, but I kept {verb[3]}.\n")
    print(f"Finally, somebody came! They {adv[0]} {verb[4]} to my mailbox.")
    print(f"I {verb[5]} out of the {noun[3]}. \"{interj[0]}!\" I shouted.")
    print(f"But it was too {adj[4]} to see. My secret {noun[5]} ran away.")
    print("I still don't know who it is!")


def madlib2_input():
    """Get words for Madlibs 2"""
    animal.append(input("\nPlease enter an animal\n> "))

    print("\nPlease enter 6 nouns (seperated by enter)")
    for _ in range(6):
        noun.append(input("> "))

    noun.append(input("\nPlease enter a plural noun\n> "))

    print("\nPlease enter 8 verbs (seperated by enter)")
    for _ in range(8):
        verb.append(input("> "))

    verb.append(input("\nPlease enter a verb ending in -ing\n> "))

    print("\nPlease enter 2 foods (seperated by enter)")
    for _ in range(2):
        food.append(input("> "))

    print("\nPlease enter 2 locations (seperated by enter)")
    for _ in range(2):
        loc.append(input("> "))

    game.append(input("\nPlease enter a game\n> "))


def madlib2():
    """Generate and print Madlibs 2"""
    madlib2_input()
    print("\n\"IF YOU GIVE A...\" MADLIB")
    print(f"If you give a {animal[0]} a {food[0]}, it is going to", end=" ")
    print(f"ask for a {noun[0]}.")
    print(f"When you give it the {noun[0]}, it will want to {verb[0]}.")
    print(f"When it is finished, it will {verb[1]}.")
    print(f"Then it will {verb[2]} and {verb[3]} to the {noun[1]}.")
    print(f"Since that doesn't work out, it will want to go to {loc[0]}.")
    print(f"On the way, it will see a {noun[2]} and will want {noun[3]}.")
    print(f"Then you will have to take it to {loc[1]}. It will {verb[4]}.")
    print(f"When it is done, it will ask for some {food[1]}.")
    print(f"On the way home, it will start a game of {game[0]}.")
    print(f"When you finally get home, you'll have to {verb[5]}.")
    print(f"Then it will want a {noun[4]}. You'll have to find", end=" ")
    print(f"a {noun[5]} and {noun[6]}.")
    print(f"When it sees the {noun[5]}, it will start {verb[8]}.")
    print(f"Then it will {verb[6]} out of {noun[6]}.")
    print(f"Of course, when it is finished, it will want to {verb[7]}.")
    print(f"So, it will ask for a {noun[0]}.")
    print(f"And chances are if you give it a {noun[0]}, it is", end=" ")
    print(f"going to want a {food[0]}.")


def madlib3_input():
    """Get words for Madlibs 3"""
    print("\nPlease enter 3 names/people (seperated by enter)")
    for _ in range(3):
        name.append(input("> "))

    game.append(input("\nPlease enter a game\n> "))

    print("\nPlease enter 2 plural nouns (seperated by enter)")
    for _ in range(2):
        noun.append(input("> "))

    animal.append(input("\nPlease enter an animal\n> "))

    print("\nPlease enter 5 verbs ending in -ing (seperated by enter)")
    for _ in range(5):
        verb.append(input("> "))

    print("\nPlease enter 3 verbs (seperated by enter)")
    for _ in range(3):
        verb.append(input("> "))

    adv.append(input("\nPlease enter an adverb\n> "))
    noun.append(input("\nPlease enter a body party\n> "))

    print("\nPlease enter 3 adjectives (seperated by enter)")
    for _ in range(3):
        adj.append(input("> "))

    loc.append(input("\nPlease enter a location\n> "))
    color.append(input("\nPlease enter a color\n> "))

    print("\nPlease enter 2 foods (seperated by enter)")
    for _ in range(2):
        food.append(input("> "))


def madlib3():
    """Generate and print Madlibs 3"""
    madlib3_input()
    print("\nTHE BIRTHDAY PARTY MADLIB")
    print(f"I'm {verb[0]} a {adv[0]} {adj[0]} party for my birthday.")
    print(f"I'm {verb[1]} my best friends, like {name[0]},", end=" ")
    print(f"{name[1]}, {name[2]}.")
    print(f"The party will be at the {loc[0]} with {adj[1]} ", end=" ")
    print(f"{noun[0]} and {color[0]} {noun[1]} for decorations.")
    print(f"First, we will {verb[5]} some snacks, like", end=" ")
    print(f"{food[0]} and {food[1]}.")
    print(f"Then we will {verb[6]} some party games like", end=" ")
    print(f"{game[0]} and {verb[7]} the {noun[2]} on the {animal[0]}.")
    print(f"Then we will {verb[6]} some party games like ", end=" ")
    print(f"and {verb[7]} the {noun[2]} on the {animal[0]}.")
    print(f"Then comes my favorite part: {verb[2]} Happy", end=" ")
    print(f"Birthday, {verb[3]} presents, and {verb[4]} some {adj[2]}.")


while True:
    print(INTRO)
    picked = int(input("Would you like to try MadLib '1' or '2' or '3'?\n> "))
    if picked == 1:
        madlib1()
    elif picked == 2:
        madlib2()
    elif picked == 3:
        madlib3()
    sys.exit()
