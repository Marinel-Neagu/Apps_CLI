import random


class GuessWord:
	def __init__(self, lives, list_words):
		self.answer = None
		self.lives = lives
		self.list_words = list_words
		self.random_word = self.word()

	
	def word(self):
		word = random.choice(self.list_words)
		return word
	
	def get_user_answer(self):
		get_answer = None
		while not get_answer:
			get_answer = input('What word do you think it is: ').strip()
		return get_answer
	
	def ask_play_user(self):
		user = None
		while not user:
			user = input('Do you want to play guess the word? Type yes or no: ').strip().lower()
		return user in ['yes', 'y']
	
	def play(self):
		print('Hello, this is a game that you have to guess the word!')
		if self.ask_play_user():
			self.check_answer()
		else:
			print('Goodbye')
	
	def check_answer(self):
		while self.lives > 0:
			print("_ " * len(self.random_word))
			self.answer = self.get_user_answer()
			if self.answer == self.random_word:
				print('A good job!')
				break
			else:
				self.lives -= 1
				print('The word is incorrect!')
				print(f'You have left with {self.lives} lives.')
		else:
			print('You lost the game!')
	def status(self):
		print(f'''
		Words guessed:
		Tries:
		Lives left:{self.lives}
		''')


game = GuessWord(lives=6, list_words=('marine', 'name', 'mere'))
game.play()
