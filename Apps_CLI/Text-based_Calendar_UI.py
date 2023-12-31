import calendar


def print_title():
    print(
        '''
             _____       _                _
            /  __ \     | |              | |
            | /  \/ __ _| | ___ _ __   __| | __ _ _ __
            | |    / _` | |/ _ \ '_ \ / _` |/ _` | '__|
            | \__/\ (_| | |  __/ | | | (_| | (_| | |
             \____/\__,_|_|\___|_| |_|\__,_|\__,_|_|
        '''
        )


def print_panel():
    print(
        ''' Press the number form the below:
            1. Calendar of the year
            2. Calendar of month
            3. Exit.'''
        )


def ask_user():
    input_user = None
    print('Do you want to see a calendar?')
    while not input_user:
        input_user = input(' Press yes/y to continue and no/n to quit:  ').strip(
                
                ).lower()
    return input_user in ['yes', 'y']


def user_choice():
    choice = None
    while not choice:
        choice = input('Press here: ')
    return choice


def valid_choice():
    while True:
        choice = user_choice()
        if choice.isdigit():
            choice = int(choice)
            return choice
        else:
            print('Please put number!')


def month_user():
    month = None
    while not month:
        month = input('Insert the number of the month like(8 or 12): ').strip()
    return month


def year_user():
    year = None
    while not year:
        year = input('Insert the number of the year like(2023): ').strip()
    return year


def month_calendar(month, year):
    print(calendar.month(year, month))


def year_calendar(year):
    print(calendar.calendar(year))


def new_choice():
    new = None
    while not new:
        new = input('Do you want to try again? Press yes/y or no/n to quit: ').strip().lower()
    return new in ['yes', 'y']


def show_calendar():
    print_title()
    print_panel()
    choice = valid_choice()
    while True:
        try:
            match choice:
                case 1:
                    year_calendar(year = int(year_user()))
                    break
                case 2:
                    month_calendar(month = int(month_user()), year = int(year_user()))
                    break
                case 3:
                    break
                case _:
                    print('Invalid number!')
        except ValueError:
            print('It has to be a number')
        except IndexError:
            print('It has to be a valid month,so you have to write a number form 1 to 12')


def main():
    while True:
        if new_choice():
            show_calendar()
        else:
            print('Goodbye')
            break


if __name__ == '__main__':
    main()
