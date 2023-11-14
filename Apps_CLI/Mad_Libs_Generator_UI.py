from time import sleep
from sys import exit


def get_user_name():
    user_name = None
    while not user_name:
        user_name = input("Please enter your name: ")
    return user_name.strip().capitalize()


def show_message(name):
    
    print("Welcome to the Mad Libs")
    sleep(2)
    print(f'Hello, {name}! Do you want to play this game?')


def user_choice():
    answer = None
    answer = input('Please press any key to start the game or type quite to exit: ')
    if answer == 'quite' or answer == 'Q':
        print('Goodbye!')
        exit()
    else:
        return True


def get_words():
    if user_choice:
        input_words()


def input_words():
    verb_1 = input('What is your first verb?: ').lower().strip()
    adj_1 = input('What is your first adjective?: ').lower().strip()
    verb_2 = input('What is second verb?: ').lower().strip()
    body_1 = input('What is your first body part?: ').lower().strip()
    adverb_1 = input('What is your first adverb?: ').lower().strip()
    body_2 = input('What is your second body part?:').lower().strip()
    noun_1 = input('What is your first noun?: ').lower().strip()
    verb_3 = input('What is your third verb?: ').lower().strip()
    noun_2 = input('What is your second noun?: ').lower().strip()
    verb_4 = input('What is your forth verb?: ').lower().strip()
    adj_2 = input('What is your second adjective?: ').lower().strip()
    color = input('What is your color?: ').lower().strip()


def clean_word(word):
    return word


def print_story():
    print(
            '''
Most doctors agree that bicycle of __verb__  is a/an __adjective__ form of exercise.
 __verb__  a bicycle enables you to develop your __part_of_body__ muscles as well as __adverb__  increase the rate of a
  __part_of_body__ beat. More __noun__ around the world __verb__  bicycles than drive __animals__.
  No matter what kind of __noun__ you __verb__, always be sure to wear a/an __adjective__ helmet.
  Make sure to have  __color__  reflectors too!
    '''
            )


def check_word(word):
    if word is not None:
        return word
    else:
        print('Please enter a valid word!')


def game():
    pass


if __name__ == '__main__':
    print('')
