import random

'''
	It puts a max limit for user to guess
'''

MAX_NUMBER = 100
MIN_NUMBER = 0


def print_title():
	print('''
    
    
 .88888.                                      oo                   
d8'   `88                                                          
88        dP    dP .d8888b. .d8888b. .d8888b. dP 88d888b. .d8888b. 
88   YP88 88    88 88ooood8 Y8ooooo. Y8ooooo. 88 88'  `88 88'  `88
Y8.   .88 88.  .88 88.  ...       88       88 88 88    88 88.  .88 
 `88888'  `88888P' `88888P' `88888P' `88888P' dP dP    dP `8888P88 
                                                               .88 
                                                           d8888P
''')


def guessing_the_number():
	computer_number = abs(random.randint(MIN_NUMBER, MAX_NUMBER))  # the computer take a random number, and it must be a
	# absolut one,not a float
	while True:  # just verify if the player guessed the number
		player_number = int(input(f'Choose a number between {MIN_NUMBER} and {MAX_NUMBER}: '))
		
		if player_number < computer_number:
			
			print('Your number is lower than the SECRET NUMBER!')
		
		elif player_number > computer_number:
			
			print('Your number is higher than the SECRET NUMBER!')
		
		else:
			print('Well done, you guessed the number!')
			break
	
	print(f'The secret number was: {computer_number}')


def new_guessing():  # it ask the user for a new round to guess
	while True:
		play_again = input('Do you want to play again, press yes to continue and q/n to quit:').lower()  # here it
		# keep asking even after the game is done
		if play_again in ['y', 'yes']:
			guessing_the_number()
		elif play_again in ['no', 'n', 'q', 'quit']:
			print('Goodbye, hope your fine!')
			break
		else:
			print('Invalid choices!')


def main():  # the main function has the both guessing_the_number and new_guessing,
	print_title()
	name = None
	while not name:
		name = input('Hello, what is your name?:  ').strip().capitalize()
	print(f'Hello, {name}. Do you want to play a guessing game?')
	
	while True:  # trying to take an error when the user put an intiger or something else
		decision = input('Type yes or no to play: ').lower()
		try:
			if decision == 'yes' or decision == 'y':
				guessing_the_number()
			elif decision in ['no', 'n', 'q', 'quit']:
				print('Okay, see you later, nerd!')
				break
		
		except ValueError:
			print('You are a schmuck! Do you hear me? You are a schmuck!!')
	return decision in ['yes']


if __name__ == '__main__':
	main()
