class CountVowelsConsonants:
	def __init__(self, sentence):
		self.sentence = sentence.lower()
		self.vowels = 'aeiou'
		self.consonants = 'bcdfghjklmnpqrstvwxyz'
	
	def count_vowels(self):
		count_vowels = 0
		for letter in self.sentence:
			if letter in self.vowels:
				count_vowels += 1
		return count_vowels
	
	def count_consonants(self):
		count_consonants = 0
		for letter in self.sentence:
			if letter in self.consonants:
				count_consonants += 1
		return count_consonants


def sentence_user():
	sentence = None
	while not sentence:
		sentence = input('Insert here a sentence, or a word: ').lower()
	return sentence


def main():
	print('To quit insert quit below or just continue to use the program.')
	while True:
		sentence = sentence_user()
		if sentence != 'quit':
			counting = CountVowelsConsonants(sentence=sentence)
			print(f'''
			Total consonants: {counting.count_consonants()}
			Total vowels: {counting.count_vowels()}
			''')
		else:
			print('Goodbye!')
			break


if __name__ == '__main__':
	main()
