def get_year_user():
    year = None
    while not year:
        year = input('What is the year you want to check: ').strip()
    return year


def check_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('This is a leap year!')
    else:
        print('This is not a leap year')


def user_choice():
    user_input = None
    while not user_input:
        user_input = input('Type yes to check a year if it is a leap year or n/no to quit: ').strip().lower()
    return user_input in ['yes', 'y']


def main():
    while True:
        try:
            choice = user_choice()
            if choice:
                user_year = get_year_user()
                check_leap_year(year = int(user_year))
            
            else:
                print('Goodbye!')
                break
        except ValueError:
            print('Sorry, you need to put a number!')


if __name__ == '__main__':
    main()
