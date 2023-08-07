# import re


def user_word():
	word_ = input('Please isert here the word to see if is a Palindrome: ').strip().lower()
	word2 = word_[::-1]
	if word2 == word_:
		print('This word is a palindrome!')
	else:
		print('This is not a palindrome word!')

if __name__ == '__main__':
	user_word()
