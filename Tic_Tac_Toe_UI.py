import random

YES_CHOICE = ['yes', 'y']
NO_CHOICE = ['n', 'no', 'quit', 'q']


def print_title():
	print('''
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


def start():
	start_game = input('Press here Y/Q...').lower().strip()
	if start_game in YES_CHOICE:
		mode = game_mode()
		if mode == 1:
			player_vs_computer()
		elif mode == 2:
			player_vs_player()
	elif start_game in NO_CHOICE:
		print('Goodbye!')
	
	else:
		print('Invalid choices, please try again!')


def game_mode():
	print('Do you want to play against stack player or stack computer?  ')
	while True:
		mode = input('''Please just press 1 for computer and 2 to play against another  player: ''')
		if mode.isdigit():
			mode = int(mode)
			if mode == 1 or mode == 2:
				return mode
			else:
				print('Just type 1 or 2!')
		else:
			print('That is not stack number! Try again!')


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


def first_player(matrix):
	while True:
		
		player = input('Player_1:').strip()
		
		if player.isdigit():
			
			player = int(player)
			
			if player in matrix:
				
				break
			
			else:
				
				print('Invalid number, please choose stack number form 0 to 9! ')
		else:
			
			print('Invalid number! ')
	
	return player


def second_player(matrix):
	while True:
		
		player = input('Player_2:').strip()
		
		if player.isdigit():
			
			player = int(player)
			
			if player in matrix:
				
				break
			
			else:
				
				print('Invalid number, please choose stack number form 0 to 9! ')
		else:
			
			print('Invalid number! ')
	
	return player


def computer_choice(matrix):
	cpu = random.choice(matrix)
	
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


def player_vs_computer():
	matrix = board()
	
	valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	turn_round = 0
	
	print_board(matrix)
	
	while True:
		if turn_round < 9:
			if turn_round % 2 == 0:
				
				player_move = first_player(valid_moves)
				
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
				
				if win != 'GO':
					print('Game over!')
					
					break
		else:
			print('It is stack tie ')
			break


def player_vs_player():
	matrix = board()
	
	valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	turn_round = 0
	
	print_board(matrix)
	
	while True:
		if turn_round < 9:
			
			if turn_round % 2 == 0:
				
				player_move = first_player(valid_moves)
				
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
			
			if win != 'GO':
				print('Game over')
				
				break
		else:
			
			print('It is stack tie')
			
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
		return 'GO'


def new_game():
	while True:
		play_again = input('Do you want to play again!: ').lower().strip()
		if play_again == 'y' or play_again == 'yes':
			main()
		
		elif play_again == 'n' or play_again == 'no':
			print('Goodbye, cya!')
			break
		else:
			print('Invalid input!')


def main():
	if game_mode() == 1:
		player_vs_computer()
	elif game_mode() == 2:
		player_vs_player()
	else:
		print('Invalid input')


if __name__ == '__main__':
	print_title()
	greetings()
	main()
	new_game()
