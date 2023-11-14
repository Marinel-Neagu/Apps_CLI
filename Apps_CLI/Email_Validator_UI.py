import re


def email_user():
    print('You have to put the email down here')
    email = input('Insert here the email: ').strip()
    while True:
        if email != '':
            print('Please insert an email!')
        else:
            return email


def checking_email():
    user_email = 'neagumarinel2014@gmail.com'
    match = re.search('[a-zA-Z0-9]', user_email)
    if match:
        print('This is good')
        print(match.group())
    else:
        print('This is bad!')


if __name__ == '__main__':
    checking_email()
