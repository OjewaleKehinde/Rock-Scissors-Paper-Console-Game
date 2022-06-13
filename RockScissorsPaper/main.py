import random

name = input("Please enter your name: ")

characters = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

options = list(characters)

# Input loop
while True:
    player  = input('Select "R" for rock, "P" for paper and "S" for scissors: ')
    CPU = random.choice(options)

    moves = print("{}({}):CPU({})".format(name, characters[player], characters[CPU]))

    if player not in options:
        print("You have not selected a valid option. Please try again\n")
    elif player == CPU:
        moves
        print("It's a tie. Please play again.\n")
    else:
        moves
        win = player + CPU
        if win in ['RS', 'PR', 'SP']:
            print('Winner: {}'.format(name))
        else:
            print('Winner: CPU')

        break


