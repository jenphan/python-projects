import sys

while True:
    secret = "apple"
    location = []
    start = 0
    guess = input("> ")
    PLAYING = True;
    attempts = 6

    for i in range(len(secret)):
        location.append(False)

    solved = False

    while PLAYING:
        start = 0
        if secret.find(guess) == -1:
            attempts -= 1
            print("-1 attempt")
            if attempts <= 0:
                print("You have run out of attempts!")
                sys.exit()
        else:
            for i in range(len(secret)):
                j = secret.find(guess, start)
                if j != -1:
                    start = j + 1
                    location[j] = True

        for x in range(len(location)):
            if x == 0:
                print("\n", end="")
            if location[x]:
                print(secret[x], end=" ")
            else:
                print("_", end=" ")

        if all(location):
            print("\nSOLVED")
            sys.exit()
        else:
            guess = input("\n> ")
    sys.exit()