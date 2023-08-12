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
	initial_sentence = sentence()
	for key, value in patterns.items():
		modified_sentence = re.sub(key, value, initial_sentence)
	print('Here is your modified sentence:',modified_sentence)

if __name__ == '__main__':
	main()
