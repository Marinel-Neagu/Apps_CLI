import re


def user_word():
	"""
		Ask the user to insert a word, or a sentence, and it must not be empty.
		
	:return:
	"""
	user_choice = None
	while not user_choice:
		user_choice = input('Please put here a word or a sentence: ')
	return user_choice


def checking_sentence(word):
	"""

	:param word:
	:return: amount of the capital word, not letters
			this will find all words that starts with capital letters and that ends with lowercase, and it repeats itself
			for each word in the sentence (this * is used to repeat)
			upper_word= re.findall(r'\b[A-Z][a-z]*\b' word)
	"""
	upper_word = re.findall(r'\b[A-Z][a-z]*\b', word)
	return len(upper_word)


def main():
	word = user_word()
	counts_words_upper = checking_sentence(word)
	print('Capital word count:', counts_words_upper)


if __name__ == '__main__':
	main()
