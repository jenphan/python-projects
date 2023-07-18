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

def madlib1_input():
    print("Please type 5 adjectives (seperated by enter)")
    for x in range(5):
        adj.append(input("> "))

    print("\nPlease enter 4 plural nouns (seperated by enter)")
    for x in range(4):
        noun.append(input("> "))
    
    print("\nPlease enter 2 nouns (seperated by enter)")
    for x in range(2):
        noun.append(input("> "))
    
    print("\nPlease enter 6 verbs (seperated by enter)")
    for x in range(6):
        verb.append(input("> "))
    
    time.append(input("\nPlease enter a time of day\n> "))
    adv.append(input("\nPlease enter an adverb\n> "))
    interj.append(input("\nPlease enter an interjection\n> "))
    

def madlib1():
    madlib1_input()
    print("\nVALENTINE'S DAY MADLIBS")
    print(f"I have a {adj[0]} admirer.")
    print(f"My admirer leaves {noun[0]} and {noun[1]} in the mailbox.")
    print(f"The letters say \"You are my {adj[1]} {noun[4]}. I want to {verb[0]}. Please be mine.\"\n")
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

while True:
    print(INTRO)
    madlib1()
    sys.exit()
