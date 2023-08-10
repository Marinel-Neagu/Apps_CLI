import re


def palindrome_checker(user_word):
	clean_word = re.sub(r'[^a-zA0-9]', '', user_word)
	clean_word = clean_word.lower()
	return clean_word == clean_word[::-1]


sentence = input('Please put a sentence, or a word to see is it a palindrome: ').strip()
if palindrome_checker(sentence):
	print('Wow, this is a palindrome word!')
else:
	print('Ops, this is not a palindrome word!')
