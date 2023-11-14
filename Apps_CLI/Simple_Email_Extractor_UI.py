import re


def get_document_user():
    """

    :return: get the name of the document
    """
    document_text = None
    while not document_text:
        document_text = input('Please insert the document name: ').strip().capitalize()
    return document_text


def read_document_user(document):
    """

    :param document:
    :return: get the text of the document, and it removes the space after the text.
    """
    with open(file = f'{document}.txt') as file:
        text_document = file.read()
        for lines in text_document:
            lines = lines.strip()
    return text_document


def email_pattern(document_text):
    """
    :param document_text:
    :return: email pattern using regex module
    """
    email = re.findall(r'[a-zA-Z0-9_+.%-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}', document_text)
    return email


def new_email_request():
    """

    :return: ask the user for putting out the emails from the document
    """
    new_request = None
    while not new_request:
        new_request = input('Type yes/y to find emails form a document or no/n to quit: ')
    return new_request in ['yes', 'y']


def main():
    """
This program just extracts all valid emails form a text
    """
    while True:
        try:
            num = 0
            if new_email_request():
                document_user = get_document_user()
                document_text = read_document_user(document_user)
                valid_email = email_pattern(document_text)
                print('Here are the all emails that I found:')
                for email in valid_email:
                    num += 1
                    print(f'Email NO {num}: {email}')
            
            else:
                print('Goodbye, and see you out there!')
                break
        except FileNotFoundError:
            print('Sorry, the name or the file is not here.')


if __name__ == '__main__':
    main()
