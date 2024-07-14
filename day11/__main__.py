import random
from art import logo

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(values):
    score = 0
    for value in values:
        score += value

    if score > 21 and 11 in values:
        values_copy = values.copy()
        while score > 21 and 11 in values_copy:
            score -= 10
            values_copy.remove(11)

    return score


def play_blackjack():
    print(logo)

    player_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), random.choice(cards)]

    print(f"  Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
    print(f"  Computers first card: {dealer_cards[0]}")

    busted = False
    while not busted and input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
        player_cards.append(random.choice(cards))
        player_score = calculate_score(player_cards)
        print(f"  Your cards: {player_cards}, current score: {player_score}")
        print(f"  Computers first card: {dealer_cards[0]}")
        busted = player_score > 21

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    while dealer_score < 17 or (dealer_score <= player_score < 21):
        dealer_cards.append(random.choice(cards))
        dealer_score = calculate_score(dealer_cards)

    print(f"  Your final hand: {player_cards}, final score: {player_score}")
    print(f"  Computer's final hand: {dealer_cards}, final score: {dealer_score}")

    if (player_score > 21 and dealer_score > 21) or player_score == dealer_score:
        print("It's a draw!")
    elif dealer_score > 21:
        print("The dealer went over. You win 😎")
    elif player_score > 21:
        print("You went over. You lose 😭")
    elif player_score > dealer_score:
        print("You have the highest score. You win 🤯")
    else:
        print("You have the lowest score. You lose 😭")

    run_game()


def run_game():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        play_blackjack()


run_game()
