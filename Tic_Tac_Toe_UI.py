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
    pass


def board():
    board_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    board_scheme = (f'''
                {board_matrix[0][0]} | {board_matrix[0][1]} | {board_matrix[0][2]}
               ___|___|___
                {board_matrix[1][0]} | {board_matrix[1][1]} | {board_matrix[1][2]}
               ___|___|___       
                {board_matrix[2][0]} | {board_matrix[2][1]} | {board_matrix[2][2]}
            ''')
    print(board_scheme)
    return board_matrix


def print_board(matrix):
    print(f'''
            {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}
           ___|___|___
            {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}
           ___|___|___       
            {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}
        ''')


def player_choice():
    while True:

        player = input('Choose a number from 1-9:').strip()
        if player.isdigit():
            player = int(player)
            if player in range(1, 10, 1):
                break
            else:
                print('Invalid number, please choose a number form 0 to 9! ')
        else:
            print('Invalid number! ')
    return player


def computer_choice(x):
    computer = random.choice(range(1, 10, 1))
    if computer not in x:
        return computer


def game():
    board_ = board()
    invalid_moves = list()
    while True:
        player_move = player_choice()

        if player_move not in invalid_moves:
            if player_move == 1:
                board_[0][0] = 'X'
            elif player_move == 2:
                board_[0][1] = 'X'
            elif player_move == 3:
                board_[0][2] = 'X'
            elif player_move == 4:
                board_[1][0] = 'X'
            elif player_move == 5:
                board_[1][1] = 'X'
            elif player_move == 6:
                board_[1][2] = 'X'
            elif player_move == 7:
                board_[2][0] = 'X'
            elif player_move == 8:
                board_[2][1] = 'X'
            elif player_move == 9:
                board_[2][2] = 'X'
            invalid_moves.append(player_move)
            computer_move = computer_choice(board_.remove(player_move))
            invalid_moves.append( )
            print(computer_move)
            if computer_move == 1:
                board_[0][0] = 'O'
                print(board_)
            elif computer_move == 2:
                board_[0][1] = 'O'
                print(board_)
            elif computer_move == 3:
                board_[0][2] = 'O'
                print(board_)
            elif computer_move == 4:
                board_[1][0] = 'O'
                print(board_)
            elif computer_move == 5:
                board_[1][1] = 'O'
                print(board_)
            elif computer_move == 6:
                board_[1][2] = 'O'
                print(board_)
            elif computer_move == 7:
                board_[2][0] = 'O'
                print(board_)
            elif computer_move == 8:
                board_[2][1] = 'O'
                print(board_)
            elif computer_move == 9:
                board_[2][2] = 'O'
                print(board_)
            print_board(board_)
        else:
            print('Invalid move! Try again')
            print_board(board_)




def valid_move():
    pass


def checking_win(matrix):
    pass


def new_game():
    pass


def main():
    pass


if __name__ == '__main__':
    game()
