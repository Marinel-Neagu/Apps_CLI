
MORSE_CODE_DICTIONARY = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                         'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                         'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                         '(': '-.--.', ')': '-.--.-'}


def get_user_text():
	text_user = None
	while not text_user:
		text_user = input('Please insert here a text: ').strip().upper()
	return text_user


def morse_translation(text):
	morse_text = ''
	for letter in text:
		morse_text += MORSE_CODE_DICTIONARY[letter] + ' ' if letter != ' ' else "  "
	print(morse_text)


if __name__ == '__main__':
	morse_translation(text=get_user_text())
