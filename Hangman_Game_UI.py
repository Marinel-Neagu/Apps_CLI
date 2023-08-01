import string
from wonderwords import *
from Hangman_pic import HANGMANPICS, TITLE


# Just say hello to the user
def hello():
	name = input('What is your name?: ').strip().capitalize()
	print(f'Hello {name}!: ')


# The game where all the action happens
def hangman():
	guessed = []
	lives = 0
	word = RandomWord()
	word_random = word.word(word_max_length=10, word_min_length=3, include_categories=['nouns'])  # random words
	# specification
	word_stage = ' _' * len(word_random)
	print(word_stage)
	
	while 0 <= lives < 7:
		letter_player = input('Choose a letter: ').strip().lower()
		
		if letter_player not in string.ascii_letters:
			print('Not a letter, type again!!!')
			continue
		
		if letter_player in word_stage:
			print('You have already guessed that letter. Just type again!', end=' ')
			guessed.append(letter_player)
			print('Letter guessed by you:', ' '.join(guessed).capitalize())
			print(word_stage)
			continue
		
		found = False
		for i in range(len(word_random)):
			if letter_player == word_random[i]:
				word_stage = word_stage[:i] + letter_player + word_stage[i + 1:]
				found = True
		
		if found:
			print(word_stage)
			print('Letter guessed by you:', ' '.join(guessed).capitalize())
		else:
			lives += 1
			print(HANGMANPICS[lives])
			print(word_stage)
			print('Wrong letter! Try again: ')
		
		if '_' not in word_stage:
			print('Congratulations! You guessed the word:', word_random)
			break
	else:
		print('The word was:', word_random)
		print('You lost the game :(!')


# The main function
def main():
	choice = input('Do you want to play hangman? Type y/n: ').strip().lower()
	
	while choice not in ['yes', 'y', 'n', 'no']:
		choice = input('Please just type y/n: ').strip().lower()
	
	if choice == 'y' or choice == 'yes':
		hangman()
	elif choice == 'n' or choice == 'no':
		print('Goodbye! Cya!')
	else:
		choice = input('Just type yes or no, man!')


if __name__ == '__main__':
	# Display game title
	print(TITLE)
	hello()
	main()
	while True:
		
		play_again = input('Do you want to play again? Pres yes or no!: ').strip().lower()
		if play_again == 'yes' or play_again == 'y':
			hangman()
		elif play_again == 'no' or play_again == 'n':
			print('Goodbye, man!')
			break
