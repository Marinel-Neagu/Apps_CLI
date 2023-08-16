import re


def get_document_user():
	document_text = None
	while not document_text:
		document_text = input('Please insert the document name: ').strip().capitalize()
	return document_text


def read_document_user(document):
	with open(file=f'{document}.txt') as file:
		text_document = file.read()
		for lines in text_document:
			lines = lines.strip()
	return text_document


def email_pattern(document_text):
	email = re.findall(r'[a-zA-Z0-9_+.%-]*@[a-zA-Z0-9]*\.[a-zA-Z]{2,6}',document_text)
	return email


def new_email_request():
	new_request = None
	while not new_request:
		new_request = input('Type yes/y to find emails form a document or no/n to quit: ')
	return new_request in ['yes', 'y']


def main():
	while True:
		if new_email_request():
			document_user = get_document_user()
			document_text = read_document_user(document_user)
			valid_email = email_pattern(document_text)
			print(valid_email)
		else:
			print('Goodbye!')
			break


if __name__ == '__main__':
	main()
