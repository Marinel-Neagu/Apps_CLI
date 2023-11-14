import csv


def get_document_user():
    """
Get the name of the document from the user
    :return:
    """
    name = None
    while not name:
        name = input('What is the name of the document: ')
    return name


def read_csv_file(name_document):
    """
Read the file using the csv library and take the content into a list for reading multiple times
    :param name_document:
    :return:
    """
    with open(f'Documents/{name_document}.csv') as file_csv:
        text_csv = csv.reader(file_csv)
        text_csv = list(text_csv)
    
    return text_csv


def print_content():
    """
Just take the list and print it out
    """
    user_document = get_document_user()
    text = read_csv_file(user_document)
    for i in text:
        print(i)


def main():
    """
Ask the user for reading the file and for a new request.
    """
    print('Do you want to read the content from a csv file?')
    
    while True:
        try:
            request = input('Press yes/y to read a file or no/n to quit: ').strip().lower()
            if request in ['yes', 'y']:
                print_content()
            elif request in ['no', 'n']:
                print('Goodbye!')
                break
            else:
                print('You have to press yes or no! Bro')
        except FileNotFoundError:
            print('File name is wrong, or the file does not exist :(')


if __name__ == '__main__':
    main()
