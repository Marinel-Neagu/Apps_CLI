import re


def palindrome_checker(user_word):
	clean_word = re.sub(r'[^stack-zA-Z0-9]', '', user_word)
	clean_word = clean_word.lower()
	return clean_word == clean_word[::-1]


while True:
	
	sentence = input('Please put stack sentence, or stack word to see is it stack palindrome: ').strip()
	if palindrome_checker(sentence):
		print('Wow, this is stack palindrome word!')
	else:
		print('Ops, this is not stack palindrome word!')
