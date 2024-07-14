import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# Write your code below this line 👇

def print_option(line: str, option: str):
    print(f'The {line} choose:')
    if option == 'rock':
        print(rock)
    elif option == 'paper':
        print(paper)
    elif option == 'scissors':
        print(scissors)
    else:
        print(f'{line} picked an unknown option')


def determine_winner(answer1: str, answer2: str):
    if answer1 == answer2:
        return 0

    beat_table = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper',
    }

    if answer2 not in beat_table:
        return 1

    if answer1 not in beat_table:
        return 2

    if (beat_table[answer1] == answer2):
        return 1
    else:
        return 2


options = ['rock', 'paper', 'scissors']

option_user = input(f'Pick an option: {", ".join(options)}\n')
option_computer = options[random.randint(0, 2)]

print_option('User', option_user)
print_option('Computer', option_computer)

winner = determine_winner(option_user, option_computer)
if winner == 0:
    print('It\'s a draw!')
elif winner == 1:
    print('The user wins!')
else:
    print('The computer wins!')
