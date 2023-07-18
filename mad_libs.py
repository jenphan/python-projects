import random
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

def madlib1_input():
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
    madlib1_input()
    print("\nVALENTINE'S DAY MADLIB")
    print(f"I have a {adj[0]} admirer.")
    print(f"My admirer leaves {noun[0]} and {noun[1]} in the mailbox.")
    print(f"The letters say \"You are my {adj[1]} {noun[4]}. " +
        f"I want to {verb[0]}. Please be mine.\"\n")
    print(f"Sometimes, my admirer leaves me chocolate with little {noun[2]} on top.")
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
    print("\nPlease enter an animal")
    animal.append(input("> "))

    print("\nPlease enter 6 nouns (seperated by enter)")
    for _ in range(6):
        noun.append(input("> "))

    print("\nPlease enter 1 plural noun")
    noun.append(input("> "))

    print("\nPlease enter 8 verbs (seperated by enter)")
    for _ in range(8):
        verb.append(input("> "))
    
    print("\nPlease enter 1 verb ending in -ing")
    verb.append(input("> "))

    print("\nPlease enter 2 foods (seperated by enter)")
    for _ in range(2):
        food.append(input("> "))
    
    print("\nPlease enter 2 locations (seperated by enter)")
    for _ in range(2):
        loc.append(input("> "))
    
    print("\nPlease enter 1 game")
    game.append(input("> "))

def madlib2():
    madlib2_input()
    print("\n\"IF YOU GIVE A...\" MADLIB")
    print(f"If you give a {animal[0]} a {food[0]}, it is going to ask for a {noun[0]}.")
    print(f"When you give it the {noun[0]}, it will want to {verb[0]}.")
    print(f"When it is finished, it will {verb[1]}.")
    print(f"Then it will {verb[2]} and {verb[3]} to the {noun[1]}.")
    print(f"Since that doesn't work out, it will want to go to {loc[0]}.")
    print(f"On the way, it will see a {noun[2]} and will want {noun[3]}.")
    print(f"Then you will have to take it to {loc[1]}. It will {verb[4]}.")
    print(f"When it is done, it will ask for some {food[1]}.")
    print(f"On the way home, it will start a game of {game[0]}.")
    print(f"When you finally get home, you'll have to {verb[5]}.")
    print(f"Then it will want a {noun[4]}. You'll have to find a {noun[5]} and {noun[6]}.")
    print(f"When it sees the {noun[5]}, it will start {verb[8]}.")
    print(f"Then it will {verb[6]} out of {noun[6]}.")
    print(f"Of course, when it is finished, it will want to {verb[7]}.")
    print(f"So, it will ask for a {noun[0]}.")
    print(f"And chances are if you give it a {noun[0]}, it is going to want a {food[0]}.")

while True:
    print(INTRO)
    rand = random.randint(1,2)
    if rand == 1:
        madlib1()
    elif rand == 2:
        madlib2()
    sys.exit()
