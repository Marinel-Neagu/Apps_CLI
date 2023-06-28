import random


def game():
    while True:
        player_number = int(input('Choose a number between 0 and 10: '))

        if player_number < computer_number:

            print('Your number is lower than the SECRET NUMBER!')

        elif player_number > computer_number:

            print('Your number is higher than the SECRET NUMBER!')

        else:
            print('Well done, you guessed the number!')
            break

    print(f'The secret number was: {computer_number}')


name = None
computer_number = abs(random.randint(0, 10))

while not name:
    name = input('Hello, what is your name?:  ')
print(f'Hello, {name.capitalize()}. Do you want to play a guessing game?')

while True:
    decision = input('Type yes or no to play: ').lower()
    try:
        if decision == 'yes':

            game()

        elif decision == 'no':
            print('Okay, see you later, nerd!')
        break

    except ValueError:
        print('You are a schmuck! Do you hear me? You are a schmuck!!')
