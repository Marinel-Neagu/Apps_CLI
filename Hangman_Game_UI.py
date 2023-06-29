from Hangman_pic import *
import string
from wonderwords import *


# Just say hello to the user
def hello():
    name = input('What is your name?: ').strip().capitalize()
    print(f'Hello {name}!: ')


 def life(): # counting for lives and implementing them
    lives = 6
    while lives > 0:
        hangman()
    else:
        print('You lost the game!')
    return lives


def new_game():
    play_again = input('Do you want to play again!').strip().lower()
    if play_again == 'y' or play_again == 'yes':
        life()
    elif play_again == 'n' or play_again == 'no':
        print('Goodbye!')


# The game where all the action happens
def hangman():
    x = 0
    word = RandomWord()
    word_random = word.word(word_max_length=10, word_min_length=3, include_categories=['nouns'])
    word_stage = ' _' * len(word_random)
    print(word_stage)

    while True:
        letter_player = input('Choose a letter: ').strip().lower()

        if letter_player not in string.ascii_letters:
            print('Not a letter, type again!!!')
            continue

        if letter_player in word_stage:
            print('You have already guessed that letter. Just type again!')
            continue

        found = False
        for i in range(len(word_random)):
            if letter_player == word_random[i]:
                word_stage = word_stage[:i] + letter_player + word_stage[i + 1:]
                found = True

        if found:
            print(word_stage)
        else:
            print(word_stage)
            print('Wrong letter! Try again.')
            print('Life')
            print(HANGMANPICS[x])

        if '_' not in word_stage:
            print('Congratulations! You guessed the word:', word_random)
            break
        return True


# The main function
def main():
    choice = input('Do you want to play hangman? Type y/n: ').strip().lower()

    while choice not in ['yes', 'y', 'n', 'no']:
        choice = input('Please just type y/n: ').strip().lower()

    if choice == 'y' or choice == 'yes':

    elif choice == 'n' or choice == 'no':
        print('Goodbye!')
    else:
        choice = input('Just type yes or no, man!')


if __name__ == '__main__':
    hello()

    main()
