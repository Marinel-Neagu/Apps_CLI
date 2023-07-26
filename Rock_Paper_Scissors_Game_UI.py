import random


def hello():
    name = None
    while not name:
        name = input('What is your name?: ').capitalize().strip()
    while True:
        print(f'Hello {name}!')
        start = input("Do you want to play a the game of Rock, Paper, Scissors? Just type yes or no: ")
        if start == 'y' or start == 'yes':
            return start in ['y', 'yes']
        elif start == 'n' or start == 'no':
            print('Goodbye!')
            break


def title():
    print(f'''
____ ____ ____ _  _      ___  ____ ___  ____ ____      ____ ____ _ ____ ____ ____ ____ ____ 
|__/ |  | |    |_/       |__] |__| |__] |___ |__/      [__  |    | [__  [__  |  | |__/ [__  
|  \ |__| |___ | \_ .    |    |  | |    |___ |  \ .    ___] |___ | ___] ___] |__| |  \ ___] 
                    '                             '                                         
''')


def rounds():
    round_game = input("How many rounds do you want to play?: ")
    if round_game.isdigit():
        round_game = int(round_game)
        return round_game
    else:
        print('You need to put a number!')


def game():
    computer_score = 0
    player_score = 0

    count = 1
    if hello():
        round = rounds()
        while round >= count:
            choice_list = ['Rock', 'Paper', 'Scissors']
            computer = random.choice(choice_list)
            player = None
            try:
                while player not in choice_list:
                    player = str(input('Chose Rock,Paper or Scissors: ')).capitalize()
                    if player == computer:
                        print('You:', player)
                        print('Computer:', computer)
                        print("It's a tie!")

                    elif player == 'Rock':
                        if computer == 'Paper':
                            computer_score += 1
                            print('You:', player)
                            print('Computer:', computer)
                            print('You lost!')

                        if computer == 'Scissors':
                            player_score += 1
                            print('You:', player)
                            print('Computer:', computer)
                            print('You won!')


                    elif player == 'Paper':
                        if computer == 'Rock':
                            player_score += 1
                            print('You:', player)
                            print('Computer:', computer)
                            print('You won!')

                        if computer == 'Scissor':
                            computer_score += 1
                            print('You:', player)
                            print('Computer:', computer)
                            print('You lost!')


                    elif player == 'Scissors':

                        if computer == 'Paper':
                            player_score += 1
                            print('You:', player)
                            print('Computer:', computer)
                            print('You won!')

                        if computer == 'Rock':
                            computer_score += 1
                            print('You:', player)
                            print('Computer:', computer)
                            print('You lost!')

            except ValueError:
                print('You have to put just words! ')
                break
            count += 1

        else:
            print('**********************************************************************************')
            print('Game Over!')
            print('Final Scores:')
            print('Player:', player_score)
            print('Computer:', computer_score)


def new_game():
    play_again = input('Do you want to play again?: ').lower().strip()
    if play_again == 'y' or play_again == 'yes':

        game()
    elif play_again == 'n' or play_again == 'no':
        print('Goodbye')


if __name__ == '__main__':
    title()
    game()
    new_game()
