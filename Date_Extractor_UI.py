import re


def extract_date(date_text):
	pattern = re.findall(r'\d{2}[./-]\d{2}[./-]+\d{4}|\d{4}[./-]\d{2}[./-]+\d{2}', date_text)
	return pattern


def read_document(document):
	with open(file=f'{document}.txt', encoding='utf-8') as file:
		text_file = file.read()
	return text_file


def get_user_document():
	user_document = None
	while not user_document:
		user_document = input('Please put here the name of the document: ').strip().capitalize()
	return user_document


def main():
	user_document = get_user_document()
	document = read_document(user_document)
	date_extracted = extract_date(document)
	print(date_extracted)


if __name__ == '__main__':
	main()
