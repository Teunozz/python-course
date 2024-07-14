# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

MAX_TRIES_EASY = 10
MAX_TRIES_HARD = 5


def run_game():
    mode = input("Do you want to play hard or easy mode? ").lower()

    if mode == "easy":
        tries = MAX_TRIES_EASY
    else:
        tries = MAX_TRIES_HARD

    goal = random.randint(0, 100)

    guessing = True
    while guessing:
        guess = int(input("Which number do you want to guess? "))

        if guess == goal:
            print("You are correct!")
            guessing = False
        else:
            tries -= 1
            tries_left = f", you have {tries} left"

        if guess < goal:
            print(f"Too low{tries_left}")
        elif guess > goal:
            print(f"Too high{tries_left}")

        if tries == 0:
            print(f"You lost, the correct number was {goal}")
            guessing = False


run_game()
