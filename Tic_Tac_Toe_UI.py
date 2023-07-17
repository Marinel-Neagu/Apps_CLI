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


def board():
    board_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    board = (f'''
                {board_matrix[0][0]} | {board_matrix[0][1]} | {board_matrix[0][2]}
               ___|______
                {board_matrix[1][0]} | {board_matrix[1][1]} | {board_matrix[1][2]}
               ___|___|___       
                {board_matrix[2][0]} | {board_matrix[2][1]} | {board_matrix[2][2]}
            ''')



def print_board():
    pass


def player_choice():
    pass


def computer_choice():
    pass


def game_mode():
    pass


def game():
    pass


def new_game():
    pass


def main():
    pass


if __name__ == '__main__':
    board()
