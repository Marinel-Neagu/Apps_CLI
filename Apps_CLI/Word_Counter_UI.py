import re


def get_user_document():
    """

    :return: name file
    """
    name_document = None
    while not name_document:
        name_document = input('Please tell me the name of the document: ').strip().lower()
    return name_document


def read_file(file_text):
    """

    :param file_text:
    :return: text from the file
    """
    with open(file = f'test_folder/{file_text}.txt') as file:
        text = file.read()
    return text


def count_words(text):
    """

    :param text: numbers of the words, not simbols included
    :return:
    """
    counter = re.findall(r'[a-zA-Z]+', text)
    return counter


def request():
    """

    :return: it returns the number for the request
    """
    user_document = get_user_document()
    text_document = read_file(user_document)
    counter = count_words(text_document)
    return len(counter)


def main():
    """
put the user into a loop and make them to choose again
    """
    print('Do you want ot count some words form a document?')
    while True:
        try:
            user_request = input('Press space to continue or no to quit: ').strip().lower()
            if user_request == 'no':
                print('Goodbye!')
                break
            else:
                print('Here is the amount the words used: ', request())
        except FileNotFoundError:
            print('There is no file, or the name is bad.')


if __name__ == '__main__':
    main()
