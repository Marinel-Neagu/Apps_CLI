MORSE_CODE_DICTIONARY = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                         'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                         'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                         '(': '-.--.', ')': '-.--.-'}


def panel():
	print('Hello, do you want to translate something in Morse Code?')
	print('''
	Press:
		1. Translate a text to Morse code.
		2. Translate a Morse code to plain text.
		3. To quit!
	''')


def ask_request():
	request = ''
	while not request.isdigit():
		request = input('Press here...').strip()
	return request


def get_user_text():
	text_user = None
	while not text_user:
		text_user = input('Please put here a text: ').strip().upper()
	return text_user


def text_to_morse(text):
	morse_text = ''
	for letter in text:
		morse_text += MORSE_CODE_DICTIONARY[letter] + ' ' if letter != ' ' else "  "
	print(morse_text)


def morse_to_text(morse):
	morse_to_text_dic = {value: key for key, value in MORSE_CODE_DICTIONARY.items()}
	word_morse = ''
	text_translated = ""
	space_tracking = 0
	for symbol in morse:
		if symbol == ' ':
			if space_tracking % 2 == 0 and word_morse:
				text_translated += morse_to_text_dic.get(word_morse, '!')
			word_morse = ''
			space_tracking += 1
		else:
			word_morse += symbol
		if space_tracking % 2 == 0 and word_morse:
			text_translated += morse_to_text_dic.get(word_morse, '!')
	print(text_translated)


def main():
	panel()
	try:
		while True:
			user_request = ask_request()
			match int(user_request):
				case 1:
					text_to_morse(get_user_text())
				case 2:
					morse_to_text(get_user_text())
				
				case 3:
					print('Goodbye')
					break
				case _:
					print('Sorry, this is an invalid choice!')
	except Exception:
		print('Please try to not scream!')


if __name__ == '__main__':
	morse_to_text(get_user_text())
