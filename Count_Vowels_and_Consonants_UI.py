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
	while True:
		sentence = sentence_user()
		counting = CountVowelsConsonants(sentence=sentence)
		print(f'''
		Total consonants: {counting.count_consonants()}
		Total vowels: {counting.count_vowels()}
		''')


if __name__ == '__main__':
	main()
