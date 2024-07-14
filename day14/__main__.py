import art
from game_data import data
import os
import random


def print_logo():
    os.system('clear')
    print(art.logo)


def print_account(letter, account):
    print(f"Compare {letter}: {account['name']}, a {account['description']}, from {account['country']}.")


def print_accounts(account_a, account_b):
    print_account("A", account_a)
    print(art.vs)
    print_account("B", account_b)


def compare_accounts(a, b):
    return a['follower_count'] > b['follower_count']


def check_answer(answer, account_a, account_b):
    if answer == 'a':
        return compare_accounts(account_a, account_b)
    elif answer == 'b':
        return compare_accounts(account_b, account_a)
    else:
        return False


def run_game():
    score = 0
    account_a = None
    active = True
    while active:
        if account_a is None:
            account_a = random.choice(data)
        account_b = random.choice(data)
        while account_b['follower_count'] == account_a['follower_count']:
            account_b = random.choice(data)

        print_logo()

        print_accounts(account_a, account_b)

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if check_answer(answer, account_a, account_b):
            score += 1
            account_a = account_b
            print(f"You're right! Current score: {score}.")
        else:
            print_logo()
            print(f"Sorry, that's wrong. Final score: {score}")
            active = False


run_game()
