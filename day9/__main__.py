import os
from art import logo

bids = {}

print(logo)
print('Welcome to the secret action program.')

action_busy = True
while action_busy:
    name = input("What is your name?: ")
    bids[name] = int(input("What's your bid?: $"))

    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "no":
        action_busy = False
        highest_bidder = ''
        highest_bid = 0

        for key in bids:
            bid = bids[key]
            if bid > highest_bid:
                highest_bidder = key
                highest_bid = bid
        print(f"The action is over, {highest_bidder} won with a bid of ${highest_bid}.")
    else:
        os.system('clear')
