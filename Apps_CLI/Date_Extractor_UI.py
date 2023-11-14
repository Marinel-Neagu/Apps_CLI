import re


def extract_date(date_text):
    pattern = re.findall(
        r'''\d{2}[./-_]\d{2}[./-_]+\d{4}  #dd.mm.yyy
                                 |
                                 \d{4}[./-_]\d{2}[./-_]+\d{2} #yyyy.mm.dd or yyyy.dd.mm
                                 |
                                 \d{2}[\s.-_]+[a-zA-Z]{3,9}[\s._-]+\d{4} #dd MONTH yyyy
                                 |
                                 [A-Z][a-z]+[\s.-_]+\d{}a-zA-Z]{2} #MONTH dd
                                 |
                                 \d{2}[\s.-_]+[a-zA-Z]+ #dd MONTH
                                 ''', date_text, re.VERBOSE
        )
    
    return pattern


def read_document(document):
    with open(file = f'{document}.txt', encoding = 'utf-8') as file:
        text_file = file.read()
    return text_file


def get_user_document():
    user_document = None
    while not user_document:
        user_document = input('Please put here the name of the document: ').strip().capitalize()
    return user_document


def request():
    new = None
    while not new:
        new = input("Do you want to a date form document, press y/yes or no/n to quit: ")
    
    return new in ['yes', 'y']


def found_date():
    user_document = get_user_document()
    document = read_document(user_document)
    date_extracted = extract_date(document)
    return date_extracted


def main():
    position = 0
    while True:
        try:
            if request():
                dates = found_date()
                if dates:
                    print('Here are all the dates that I found!')
                    for date in dates:
                        position += 1
                        print(f'Date NO{position}: {date}')
                else:
                    print('Sorry, I did not find something good here!')
            else:
                
                print('Goodbye, see you out there!')
                break
        except FileNotFoundError:
            print('This is not here')


if __name__ == '__main__':
    main()
