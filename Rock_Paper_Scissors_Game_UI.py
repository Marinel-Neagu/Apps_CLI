import random


def game():
    computer_score = 0
    player_score = 0
    rounds = 0

    while rounds < total:

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
        rounds += 1

    else:
        print('**********************************************************************************')
        print('Game Over!')
        print('Final Scores:')
        print('Player:', player_score)
        print('Computer:', computer_score)


while True:
    try:
        total = int(input('How many rounds do you want to play!: '))
        game()
        play_again = input('Do you want to play again! [y/n]:').lower()
        if play_again == 'y':
            game()
        elif play_again == 'n':
            print('Goodbye!')
            break
        else:
            print('Choose just yes or no!')

    except ValueError:
        print("Sorry put just a number!")
