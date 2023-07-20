import time

def countdown(t):
    print()
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("TIMER UP")

INTRO = """(´• ω •`) ♡ WELCOME TO COUNTDOWN TIMER! (´ε｀ )♡
When prompted, type how many minutes and seconds you
would like to set the countdown timer for.
"""

print(INTRO)

MIN = int(input("Enter minutes: "))
SEC = int(input("Enter seconds: "))
TIME = SEC + (MIN * 60)
countdown(TIME)