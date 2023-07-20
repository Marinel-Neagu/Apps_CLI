import random


def title():
    print(f'''
.___________. __    ______    .___________.    ___       ______    .___________.  ______    _______ 
|           ||  |  /      |   |           |   /   \     /      |   |           | /  __  \  |   ____|
`---|  |----`|  | |  ,----'   `---|  |----`  /  ^  \   |  ,----'   `---|  |----`|  |  |  | |  |__   
    |  |     |  | |  |            |  |      /  /_\  \  |  |            |  |     |  |  |  | |   __|  
    |  |     |  | |  `----.       |  |     /  _____  \ |  `----.       |  |     |  `--'  | |  |____ 
    |__|     |__|  \______|       |__|    /__/     \__\ \______|       |__|      \______/  |_______| 
''')


def greetings():
    name = None
    print('Hello, how are you? I want to tell you thank you for playing with me, so lets start.')
    while not name:
        name = input('What is your name?: ').capitalize().strip()

    print(f'Alright {name},do you want to play Tic Tac Toe? If yes just press y  or to quit just press q.')
    while True:
        start = input('Press here...').lower().strip()
        if start == 'y' or start == 'yes':
            start_game = True
            break
        if start == 'q' or start == 'quit' or start == 'n' or start == 'no':
            start_game = False
            break

        else:
            print('Invalid choices, please try again!')
    return start_game


def game_mode():
    print('Do you want to play against a player or a computer?  ')
    while True:
        mode = input(f'''Please just press 1 for computer and 2 to play against another  player: ''')
        if mode.isdigit():
            mode = int(mode)
            if mode == 1 or mode == 2:
                return mode
            else:
                print('Just type 1 or 2!')
        else:
            print('That is not a number! Try again!')


def board():
    board_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return board_matrix


def print_board(matrix):
    print(f'''
            {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}
           ___|___|___
            {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}
           ___|___|___       
            {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}
        ''')


def first_player():
    while True:

        player = input('Player_1(Choose a number from 1-9):').strip()
        if player.isdigit():
            player = int(player)
            if player in range(1, 10, 1):
                break
            else:
                print('Invalid number, please choose a number form 0 to 9! ')
        else:
            print('Invalid number! ')
    return player


def second_player(list):
    while True:

        player = input('Player_2(Choose a number from 1-9):').strip()
        if player.isdigit():
            player = int(player)
            if player in list:
                break
            else:
                print('Invalid number, please choose a number form 0 to 9! ')
        else:
            print('Invalid number! ')
    return player


def computer_choice(list):
    cpu = random.choice(list)
    return cpu


def modified_board(matrix, num, turn):
    if num == 1:
        matrix[0][0] = turn
    elif num == 2:
        matrix[0][1] = turn
    elif num == 3:
        matrix[0][2] = turn
    elif num == 4:
        matrix[1][0] = turn
    elif num == 5:
        matrix[1][1] = turn
    elif num == 6:
        matrix[1][2] = turn
    elif num == 7:
        matrix[2][0] = turn
    elif num == 8:
        matrix[2][1] = turn
    elif num == 9:
        matrix[2][2] = turn
    return matrix


def game_bot():
    matrix = board()
    valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn_round = 0
    print_board(matrix)
    while turn_round <= 9:
        if turn_round % 2 == 0:
            player_move = first_player()
            if player_move in valid_moves:

                modified_board(matrix, player_move, 'X')

                valid_moves.remove(player_move)

                turn_round += 1
            else:
                print('Invalid Move, try again!')

        if turn_round % 2 != 0 and turn_round < 9:
            computer_move = computer_choice(valid_moves)

            modified_board(matrix, computer_move, 'O')

            valid_moves.remove(computer_move)
            turn_round += 1
            print_board(matrix)
            win = checking_win(matrix)
            if win != 'STOP':
                print('Game over!')
                break


        else:
            print('It is a tie ')
            break


def game_player():
    matrix = board()
    valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn_round = 0
    print_board(matrix)
    while turn_round <= 9:
        if turn_round % 2 == 0:
            player_move = first_player()
            if player_move in valid_moves:

                modified_board(matrix, player_move, 'X')

                valid_moves.remove(player_move)

                turn_round += 1
                print_board(matrix)
            else:
                print('Invalid Move, try again!')

        if turn_round % 2 != 0 and turn_round < 9:
            second_player_move = second_player(valid_moves)

            modified_board(matrix, second_player_move, 'O')

            valid_moves.remove(second_player_move)
            turn_round += 1
            print_board(matrix)
            win = checking_win(matrix)
            if win != 'STOP':
                print('Game over!')
                break





def checking_win(matrix):
    if matrix[0][0] == 'X' and matrix[0][1] == 'X' and matrix[0][2] == 'X':
        print("X has won!")
        return "X"
    elif matrix[0][0] == 'O' and matrix[0][1] == 'O' and matrix[0][2] == 'O':
        print("O has won!")
        return "O"
    elif matrix[1][0] == 'X' and matrix[1][1] == 'X' and matrix[1][2] == 'X':
        print("X has won!")
        return "X"
    elif matrix[1][0] == 'O' and matrix[1][1] == 'O' and matrix[1][2] == 'O':
        print("O has won!")
        return "O"
    elif matrix[2][0] == 'X' and matrix[2][1] == 'X' and matrix[2][2] == 'X':
        print("X has won!")
        return "X"
    elif (matrix[2][0] == 'O' and matrix[2][1] == 'O' and matrix[2][2] == 'O'):
        print("O has won!")
        return "O"
    ### Y axis
    if matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X':
        print("X has won!")
        return "X"
    elif matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O':
        print("O has won!")
        return "O"
    elif matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X':
        print("X has won!")
        return "X"
    elif matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O':
        print("O has won!")
        return "O"
    elif matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X':
        print("X has won!")
        return "X"
    elif matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O':
        print("O has won!")
        return "O"

    elif matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X':
        print("X has won!")
        return "X"
    elif matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O':
        print("O has won!")
        return "O"
    elif matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X':
        print("X has won!")
        return "X"
    elif matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O':
        print("O has won!")
        return "O"
    else:
        return 'STOP'


def new_game():
    while True:
        play_again = input('Do you want to play again!: ').lower().strip()
        if play_again == 'y' or play_again == 'yes':
            game()
        if play_again == 'n' or play_again == 'no':
            print('Goodbye, cya!')
            break
        else:
            print('Invalid input!')


def main():
    pass


if __name__ == '__main__':
    game_player()
