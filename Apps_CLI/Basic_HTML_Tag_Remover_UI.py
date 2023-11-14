import re


def get_user_html():
    """
Get the name of the file form the user
    :return:
    """
    html_text = None
    while not html_text:
        html_text = input('Please put here the name of the document: ').strip()
    return html_text


def read_html(document):
    """
It reads the document from the user
    :param document:
    :return:text of the document
    """
    with open(file = f'test_folder/{document}.txt') as file:
        text = file.read()
    return text


def tags_remover(text):
    """
    :param text: from the user
    :return: remove all the tag from the text
    """
    pattern = re.sub(r'<.*?>', '', text)
    return pattern


def clean_pattern(text):
    """
    :param text:
    :return: just remove the spaces that are in execs, like the tabs.
    """
    pattern = re.sub(r'\s+', ' ', text)
    return pattern.strip()


def request():
    """

    :return: return the clean text that the user can use
    """
    try:
        user_html = get_user_html()
        read_file = read_html(user_html)
        clean_tags = tags_remover(read_file)
        clean_user_text = clean_pattern(clean_tags)
        return clean_user_text
    except FileNotFoundError:
        print('The file is not here or the name is wrong!')


def main():
    """
Main, ask the user for a request
    """
    while True:
        new = input('Do you want to clean some HTML code? Press enter to continue or no to quit:')
        if new != 'no':
            print(request())
        else:
            print('Goodbye')
            break


if __name__ == '__main__':
    main()
