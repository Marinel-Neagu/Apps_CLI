import random


def row_user():
    while True:
        try:
            row = int(input('Please choose a row: ').strip())
            if 0 <= row <= 2:
                return row
            else:
                print('Please just chose a row from 0-2!')
        except ValueError:
            print('Invalid choice! Please try again!')


def column_user():
    while True:
        try:
            column = int(input('Please choose a column: ').strip())
            if 0 <= column <= 2:
                return column
            else:
                print('Please just chose a column from 0-2!')
        except ValueError:
            print('Invalid choice! Please try again!')


def symbol_user():
    while True:
        try:
            symbol = input('Please choose a symbol(X or O):').capitalize().strip()
            if symbol in ['X', 'O']:
                return symbol
            else:
                print('Please just chose a symbol(X or O)!: ')
        except ValueError:
            print('Invalid choice! Please try again!')


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
    print(f'''
              |   | 
           ___|___|___
              |   | 
           ___|___|___       
              |   |
        ''')
    while True:

        board = (f'''
            {board_matrix[0][0]} | {board_matrix[0][1]} | {board_matrix[0][2]}
           ___|___|___
            {board_matrix[1][0]} | {board_matrix[1][1]} | {board_matrix[1][2]}
           ___|___|___       
            {board_matrix[2][0]} | {board_matrix[2][1]} | {board_matrix[2][2]}
        ''')
        print(board)
        row = row_user()
        column = column_user()
        symbol = symbol_user()
        if board_matrix[row][column] !=' ':
            print('Please choose another place!')
        else:
            board_matrix[row][column] = symbol

        if board_matrix[0]


def game():
    pass


def main():
    if hello():
        game()
    else:
        print('Goodbye, see you later!')


if __name__ == '__main__':
    game_board()
