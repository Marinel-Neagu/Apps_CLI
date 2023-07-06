import random


def title():
    print(f'''
    
    
 .88888.                                      oo                   
d8'   `88                                                          
88        dP    dP .d8888b. .d8888b. .d8888b. dP 88d888b. .d8888b. 
88   YP88 88    88 88ooood8 Y8ooooo. Y8ooooo. 88 88'  `88 88'  `88 
Y8.   .88 88.  .88 88.  ...       88       88 88 88    88 88.  .88 
 `88888'  `88888P' `88888P' `88888P' `88888P' dP dP    dP `8888P88 
                                                               .88 
                                                           d8888P
''')


def game():
    computer_number = abs(random.randint(0, 10))  # the computer take a random number, and it must be a absolut one,
    # not a float
    while True:  # just verify if the player guessed the number
        player_number = int(input('Choose a number between 0 and 10: '))

        if player_number < computer_number:

            print('Your number is lower than the SECRET NUMBER!')

        elif player_number > computer_number:

            print('Your number is higher than the SECRET NUMBER!')

        else:
            print('Well done, you guessed the number!')
            break

    print(f'The secret number was: {computer_number}')


def new_game():  # new game is on

    play_again = None
    while not play_again:  # it make the user to not press a empty answer, and it make to keep try it
        while True:
            play_again = input('Do you want to play again, press yes to continue and q to quit:').lower()  # here it
            # keep asking even after the game is done
            if play_again == 'yes' or play_again == 'y':
                game()
            if play_again == 'q' or play_again == 'quit':
                print('Goodbye, hope your fine!')
                break


def main():  # the main function has the both new_game and game,
    title()
    name = None
    while not name:
        name = input('Hello, what is your name?:  ')
    print(f'Hello, {name.capitalize()}. Do you want to play a guessing game?')

    while True:  # trying to take an error when the user put an intiger or something else
        decision = input('Type yes or no to play: ').lower()
        try:
            if decision == 'yes' or decision == 'y':
                game()
                new_game()

            if decision == 'no' or decision == 'n':
                print('Okay, see you later, nerd!')
            break

        except ValueError:
            print('You are a schmuck! Do you hear me? You are a schmuck!!')
    return decision in ['yes']


if __name__ == '__main__':
    main()
