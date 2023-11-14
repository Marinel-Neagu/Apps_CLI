"""

The program is done but must implement some validation
for checking if the date is valid, not just the format.

"""
import re

time_patterns = {'DD': r'\d{2}', 'MM': r'\d{2}', 'YYYY': r'\d{4}'}


def get_user_time():
    """

    :return: return the time or date from the user
    """
    user_time = None
    while not user_time:
        user_time = input('Please put here a date to check it if it is good or not: ').strip()
    return user_time


def get_user_format():
    """

    :return:ask the user for a format date
    """
    type_data = None
    while not type_data:
        type_data = input('Please tell me what the format do you want to check: ').strip().upper()
    return type_data


def format_time(time_string):
    """

    :param time_string:
    :return:it replaces the DD, MM and YYYY with regular expression for checking the date
    """
    for key, value in time_patterns.items():
        time_string = time_string.replace(key, value)
    return time_string


def checking_time():
    """
    It takes the user date and format, and then it checks if it a valid.
    """
    
    user_time = get_user_time()
    user_format = get_user_format()
    pattern = format_time(user_format)
    valid_time = re.match(pattern, user_time)
    if valid_time:
        print('This date is a valid one')
    else:
        print('This is a a bad one')


def request_new_date_format():
    """

    :return: Ask the user for a new request
    """
    new_date = None
    while not new_date:
        new_date = input('Do you want to try a new date? Press y/yes or n/no to quit: ')
    return new_date in ['yes', 'y']


def main():
    """
Put together the checking_time function and the new_request
    """
    checking_time()
    while request_new_date_format():
        checking_time()
    print('Goodbye')


if __name__ == '__main__':
    main()
