import re


def document():
	while True:
		user_document = input('Please put here the name of the document: ').strip().capitalize()
		if user_document != '':
			return user_document
		else:
			print('Please put the name of the document!')


def clear_text(text):
	clean_text = re.sub(r'\s+', ' ', text)
	return clean_text


def clear_document():
	while True:
		try:
			user_document = document()
			with open(f'{user_document}.txt') as file:
				text = file.read()
				clean = clear_text(text)
			
			with open(f'{user_document}.txt', 'w') as file:
				file.write(clean)
				break
		except FileNotFoundError:
			print("Sorry, this file doesn't exist!")
		except Exception:
			print('Sorry, this is a bad news for me :(')
	
if __name__ == '__main__':
	clear_document()
