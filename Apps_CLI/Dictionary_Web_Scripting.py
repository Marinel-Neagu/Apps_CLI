import time

import requests
from bs4 import BeautifulSoup


def get_user_word():
    user_sentence = None
    while not user_sentence:
        user_sentence = input('Please insert here a word, or a sentence that you want to know about: ').strip()
    return user_sentence


def request_site_status():
    time.sleep(1)
    site_request = requests.get('https://dexonline.ro')
    print('The status of the code: ', site_request.status_code)
    print('The site is:', 'GOOD' if site_request.ok else 'BAD')


def site_source(user_word):
    time.sleep(1)
    source = requests.get(f'https://dexonline.ro/definitie/{user_word}').text
    soup_site = BeautifulSoup(source, 'lxml')
    return soup_site


def get_definition(site):
    definition = site.find('span', class_ = 'def html').text
    return definition


def ask_user():
    ask = None
    while not ask:
        ask = input(
                'Do you want to find a definition for a word? Press yes/y to continue or no/n to quit: '
                ).strip().lower()
    return ask in ['yes', 'y']


def show_definiton():
    try:
        user_word = get_user_word()
        site = site_source(user_word)
        definition = get_definition(site)
        print('Definitia este:', definition.strip())
    except AttributeError:
        print('Sorry this word is not in my dex :(')


def main():
    request_site_status()
    while True:
        if ask_user():
            show_definiton()
        else:
            print('It is ok, have a nice day!')
            break


if __name__ == '__main__':
    main()
