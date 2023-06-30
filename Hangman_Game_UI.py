
import string
from wonderwords import *
import Hangman_pic


# Just say hello to the user
def hello():
    name = input('What is your name?: ').strip().capitalize()
    print(f'Hello {name}!: ')


# The game where all the action happens
def hangman():
    x = 0
    lives = 6
    word = RandomWord()
    word_random = word.word(word_max_length=10, word_min_length=3, include_categories=['nouns'])
    word_stage = ' _' * len(word_random)
    print(word_stage)

    while lives > 0:
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
                print(HANGMANPICS[x])

        if found:
            print(word_stage)
        else:
            lives -= 1
            x += 1
            print(HANGMANPICS[x])
            print(word_stage)
            print('Wrong letter! Try again.')
            print('Lives left:', lives)

        if '_' not in word_stage:
            print('Congratulations! You guessed the word:', word_random)
            break
    else:
        print('You lost the game :(')


# The main function
def main():
    choice = input('Do you want to play hangman? Type y/n: ').strip().lower()

    while choice not in ['yes', 'y', 'n', 'no']:
        choice = input('Please just type y/n: ').strip().lower()

    if choice == 'y' or choice == 'yes':
        hangman()
    elif choice == 'n' or choice == 'no':
        print('Goodbye!')
    else:
        choice = input('Just type yes or no, man!')


if __name__ == '__main__':

    print(f''' 
         __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
        |  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
        |  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
        |   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
        |  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
        |__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|
        ''')
    hello()
    main()

