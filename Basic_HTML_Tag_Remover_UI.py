import re


def get_HTML():
	HTML_TEXT = None
	while not HTML_TEXT:
		HTML_TEXT = input('Plese put here the name of the document: ').strip()
	return HTML_TEXT


def HTML_file(document):
	with open(file=f'test_folder/{document}.txt') as file:
		text = file.read()
	return text

def clean_pattern(text):
	pattern = re.sub(r'<.*?>', '', text)
	return pattern


def main():
	user_html = get_HTML()
	read_file = HTML_file(user_html)
	clean_text = clean_pattern(read_file)
	print(clean_text)


if __name__ == '__main__':
	main()
