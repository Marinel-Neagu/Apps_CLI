BOARD = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0], [0, 0, 1, 0, 5, 0, 9, 3, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]


class SudokuSolver:
	def __init__(self, board):
		self.board = board
	
	def print_board(self):
		for row in range(len(self.board)):
			if row % 3 == 0 and row != 0:
				print('_ _ _ _ _ _ _ _ _ _ ')
			for column in range(len(self.board[0])):
				if column % 3 == 0 and column != 0:
					print('|', end='')
				if column != 8:
					print(self.board[row][column], end=' ')
				else:
					print(self.board[row][column])
	
	def find_empty(self):
		for row in range(len(self.board)):
			for column in range(len(self.board[0])):
				if self.board[row][column] == 0:
					return row, column
		return None

	def solved(self):
		find = self.find_empty()
		if find:
			row, column = find
		else:
			return True
			
	
	
	
	def valid_board(self):
		for row in range(len(self.board)):
			if self.board[]
			

def main():
	sudoku = SudokuSolver(board=BOARD)
	sudoku.print_board()


if __name__ == '__main__':
	main()
