import random


def hello():
    while True:
        name = input('Hello, what is your name: ').capitalize().strip()
        if name.isdigit() or name == '':
            print('Please choose a valid name!')
        else:
            print(f'Hello {name}! Do you want to play a Tic Tac Toe match?')
            choice = input('Just press y to play and q to quit...').lower()
            break
    return choice in ['y', 'yes']


def game_board():
    board_matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    while True:
        board = f'''
                {board_matrix[0][0]} | {board_matrix[0][1]} | {board_matrix[0][2]}
               ___|___|___
                {board_matrix[1][0]} | {board_matrix[1][1]} | {board_matrix[1][2]}
               ___|___|___       
                {board_matrix[2][0]} | {board_matrix[2][1]} | {board_matrix[2][2]}
            '''
        print(board)

        row = int(input('Row'))
        column = int(input('Column'))
        symbol = input('Symbol')
        board_matrix[row][column] = symbol



def game():
    pass


def main():
    if hello():
        game()
    else:
        print('Goodbye, see you later!')


if __name__ == '__main__':
    game_board()
