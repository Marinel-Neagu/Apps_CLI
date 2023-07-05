import random

import random


def magic_ball_answer():
    # Store the magic ball answers as a multi-line string
    magic_ball_words = f'''
        It is certain
        It is decidedly so
        Without a doubt
        Yes definitely
        You may rely on it
        As I see it, yes
        Most likely
        Outlook good
        Yes
        Signs point to yes
        Reply hazy, try again
        Ask again later
        Better not tell you now
        Cannot predict now
        Concentrate and ask again
        Don’t count on it
        My reply is no
        My sources say no
        Outlook not so good
        Very doubtful
        '''

    # Generate a list of magic numbers
    magic_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Split the multi-line string into a list of magic ball answers
    magic_ball_words = magic_ball_words.strip().splitlines()

    # Create a dictionary where magic numbers are keys and magic ball answers are values
    answers = dict(zip(magic_numbers, magic_ball_words))

    # Select a random magic number and assign its corresponding answer to the variable 'key'
    for key, value in answers.items():
        key = random.choice(magic_numbers)

    # Return the selected magic ball answer, stripped and capitalized
    return answers[key].strip().capitalize()


def user_question():
    question = None
    while not question:
        question = input('Ask me a question:').lower()
    return question


def main():
    while True:
        question = user_question()
        if question == 'q' or question == 'quit':
            print('Goodbye, I hope it worked my game!')
            break
        else:
            print('The ball said:', magic_ball_answer() + '.')


def new_session():
    new_game = None
    print(f'Do you want to play again with me?')

    while not new_game:
        new_game = input('Type yes for start a new session, and q for leaving:')
    while True:
        if new_game == 'y' or new_game == 'yes':
            main()
        if new_game == 'q' or new_game == 'quit':
            print('Goodbye for now, I hope that you heard what you wanted to hear!')
            break
        else:
            print('You have to put just yes or q/quit!')
            new_game = input('Type yes for start a new session, and q for leaving:')


def title():
    print(f'''
        $$\      $$\                     $$\                  $$$$$$\        $$$$$$$\            $$\ $$\ 
        $$$\    $$$ |                    \__|                $$  __$$\       $$  __$$\           $$ |$$ |
        $$$$\  $$$$ | $$$$$$\   $$$$$$\  $$\  $$$$$$$\       $$ /  $$ |      $$ |  $$ | $$$$$$\  $$ |$$ |
        $$\$$\$$ $$ | \____$$\ $$  __$$\ $$ |$$  _____|       $$$$$$  |      $$$$$$$\ | \____$$\ $$ |$$ |
        $$ \$$$  $$ | $$$$$$$ |$$ /  $$ |$$ |$$ /            $$  __$$<       $$  __$$\  $$$$$$$ |$$ |$$ |
        $$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$ |$$ |            $$ /  $$ |      $$ |  $$ |$$  __$$ |$$ |$$ |
        $$ | \_/ $$ |\$$$$$$$ |\$$$$$$$ |$$ |\$$$$$$$\       \$$$$$$  |      $$$$$$$  |\$$$$$$$ |$$ |$$ |
        \__|     \__| \_______| \____$$ |\__| \_______|       \______/       \_______/  \_______|\__|\__|
                               $$\   $$ |                                                                
                               \$$$$$$  |                                                                
                                \______/''')


def hello():
    name = input('What is your name:').strip().capitalize()
    print(f'''
                Hello,{name}.Do you want to play with this program?
                To exit just press Q/q or if you want play just follow the message below!
    ''')


if __name__ == '__main__':
    title()
    hello()
    main()
    new_session()
