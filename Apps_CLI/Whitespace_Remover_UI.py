import re


def document():
    """
It takes the path of the document from the user
    :return:user_document
    """
    while True:
        user_document = input('Please put here the name of the document: ').strip().capitalize()
        if user_document != '':
            return user_document
        else:
            print('Please put the name of the document!')


def clear_text(text):
    """

    :param text:
    :return: clean text, without the empty space that is unnecessary.
    """
    clean_text = re.sub(r'\s+', ' ', text)
    return clean_text


def clear_document():
    """
    It opens the document, and then it pastes the clean text.
    """
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
            print('Sorry, this is bad news for me :(')


def main():
    clear_document()
    while True:
        new_document = input('Do you want to clear a new document, press y/yes or n/no.')
        if new_document == 'yes' or new_document == 'y':
            clear_document()
        else:
            print('Goodbye, have a nice day')
            break


if __name__ == '__main__':
    main()
