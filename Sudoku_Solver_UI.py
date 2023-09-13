GRID = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def print_board(board):
	for row in range(0, 9):
		if row % 3 == 0 and row != 0:
			print('_ _ _ _ _ _ _ _ _ _ _ _')
		for column in range(0, 9):
			if column % 3 == 0 and column != 0:
				print("|", end=' ')
			if column == 8:
				print(board[row][column])
			else:
				print(board[row][column], end=' ')


def find_empty(board):
	for row in range(0, 9):
		for column in range(0, 9):
			if board[row][column] == 0:
				return row, column
	return None


def valid_board(board, number, empty_position):
	for row in range(0, 9):
		if board[row][empty_position[1]] == number and empty_position[1] != row:
			return False
	
	for column in range(0, 9):
		if board[empty_position[0]][column] == number and empty_position[0] != column:
			return False
	
	box_row = empty_position[0] // 3
	box_column = empty_position[0] // 3
	for row in range(box_row * 3, box_row * 3 + 3):
		for column in range(box_column * 3, box_column * 3 + 3):
			if board[row][column] == number:
				return False
	return None

def solve(board):
	find = find_empty(board)
	if find:
		return True
	else:
		row,column =find
		re


def main():
	print_board(GRID)


if __name__ == '__main__':
	main()
