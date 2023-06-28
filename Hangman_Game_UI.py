import random
import string


# just say hello to user
def hello():
    name = input('What is your name?: ').strip().capitalize()
    print(f'Hello {name}!')


# the game
def hangman():
    list_words = ['car', 'mouse', 'cat']
    word_random = random.choice(list_words)
    status = '_' * len(word_random)
    final_status= status
    print(status)
    letter_player = ''

for i in range(status):
    if status[i]=='_':

    while letter_player in string.ascii_letters:
        letter_player = input('Choose  letter: ').strip().lower()
        for i in range(len(word_random)):
            if letter_player == word_random[i]:
                status = status[:i] + letter_player + status[i + 1:]



# the main
def main():
    choice = input('Do you want to play hangman? Type y/n: ').strip().lower()
    while choice not in ['yes', 'y', 'n', 'no']:
        choice = input('Please just type y/n: ').strip().lower()
    if choice == 'y' or choice == 'yes':
        hangman()
    if choice == 'n' or choice == 'no':
        print('Goodbye!')

    else:
        choice = input('Just type yes or no, man!')


if __name__ == '__main__':
    hello()
    main()
