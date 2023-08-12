import re

patterns = {r'\bfirst_name\b': 'Michel', r'\blast_name\b': 'Jackson', r'\bjob\b': 'Lazy Mann'}


def sentence():
	"""
	:return: user_sentence
	"""
	user_sentence = None
	while not user_sentence:
		user_sentence = input('Please insert here a sentence: ').strip()
	return user_sentence


def main():
	"""
		Take the pattern and the new word from the patterns' dictionary and print it out.
	"""
	user_sentence = sentence() # discord helped a lot :)
	for key, value in patterns.items():
		user_sentence = re.sub(key, value, user_sentence)
	print('Here is your modified sentence:', user_sentence)


if __name__ == '__main__':
	main()
