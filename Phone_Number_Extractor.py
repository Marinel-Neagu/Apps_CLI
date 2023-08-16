import re
import time

def name_document():
	name = None
	while not name:
		name = input('Please put the name of the document: ').strip().capitalize()
	return name


def clean_text(sentence):
	clean_sentence = re.sub(r'[^a-zA-Z0-9]', '', sentence)
	return clean_sentence


def phone_number(sentence):
	phone_match = re.findall(r'07[2-8]\d{7}|407[2-8]\d{7}', sentence)
	return phone_match


def read_document(document):
	with open(file=f'{document}.txt') as file:
		text_document = file.read()
	return text_document


def main():
	while True:
		print('Do you want to search into a document after some phone numbers?')
		ask_user = input('Press here yes/y or n/no to quit: ')
		if ask_user in ['yes', 'y']:
			try:
			
				count = 0
				user_document = name_document()
				text = read_document(user_document)
				text_clean = clean_text(text)
				find_phone_number = phone_number(text_clean)
				if find_phone_number:
					print('Here are the numbers that I find:')
					time.sleep(3)
					for i in find_phone_number:
						count += 1
						print(f'Phone number {count}: {i} ')
				else:
					print('Sorry, there is not a single phone number in your document.')
			
			except FileNotFoundError:
				print('The name of the file is wrong or the file does not exist.')
		else:
			print('Goodbye!')
			break

if __name__ == '__main__':
	main()
