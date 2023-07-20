import sys
import math

def is_perfect_square(num):
    root = int(math.sqrt(num))
    return root * root == num

def is_fibonacci(num):
    if is_perfect_square(5 * num * num * 4) or is_perfect_square(5 * num * num - 4):
        print(f"{NUM} is a fibonacci number.\n")
    else:
        print(f"{NUM} is NOT a fibonacci number.\n")

def validate_num(num):
    if num.isdecimal():
        is_fibonacci(int(num))
    else:
        print("Please use a valid number.\n")

INTRO = """(´• ω •`) ♡ WELCOME TO THE FIBONACCI CHECKER! (´ε｀ )♡
Type a number to check whether it is part of the fibonnaci sequence.
Type 'quit' to stop the program.
"""

if __name__ == "__main__":
    print(INTRO)
    while True:
        NUM = input("> ")
        if NUM == 'quit':
            sys.exit()
        else:
            validate_num(NUM)


