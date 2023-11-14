import datetime
import sys


def show_panel():
    print(
        '''
        1. Show user
        2. Show money
        3. Deposit
        4. Withdraw
        5. Benefits.
        6. Show panel
        7. Exit Bank Simulator.
            '''
        )


def user_amount():
    while True:
        amount = input('Insert here the money: ').strip()
        if amount.isdigit():
            amount = int(amount)
            return amount
        else:
            print('Please put a number!')


def name_user():
    name = None
    while not name:
        name = input('What is your name: ').strip().capitalize()
    return name


def type_account_user():
    print(
        '''
            Premium Account-price = 999.99 lei
            ClassicAccount Account-price = 69.99 lei'''
        )
    while True:
        ask_user = input(
                'Do you want to buy a ClassicAccount or Premium account? Write classic or premium: '
                ).strip().lower()
        if ask_user in ['classic', 'premium']:
            match ask_user:
                case 'classic':
                    return 'Classic'
                case 'premium':
                    return 'Premium'
                case _:
                    print('Invalid option')


def birth_user():
    print('We need your birthdate!')
    while True:
        try:
            user_year = input('In what year did you born?: ').strip()
            user_month = input('In what month did you born?: ').strip()
            user_day = input('On what day did you born?: ').strip()
            if datetime.datetime(year = int(user_year), month = int(user_month), day = int(user_day)):
                birth = f'{user_day}.{user_month}.{user_year}'
                return birth
            else:
                print('Invalid date!')
        except ValueError:
            print('Invalid date! Try again!!')


class Bank:
    id = 'UGLIFYJS78JJ'
    
    def __init__(self, money, date_of_birth, name, account, rate = 19):
        self.rate = rate / 100
        self.name = name
        self.type_account = account
        self.money = money
        self.date = date_of_birth
    
    def info_user(self):
        print(
            f'''
		Name: {self.name}
		Date of birth:{self.date}
		Money in deposit:{self.money}
		Type of account: {self.type_account}
		Rate: {self.rate} lei
		Id: {self.id}
		'''
            )
    
    def check_balance(self):
        print(f'Your balance is: {self.money} lei')
    
    def withdraw(self, amount):
        self.money -= amount + self.rate
        print(
            f'''
		You withdraw from your bank account {amount} lei
		You balance is now:{self.money} lei
		'''
            )
    
    def deposit(self, amount):
        self.money += amount
        print(f'You deposit in your bank account {self.money} lei')


class PremiumAccount(Bank):
    
    def withdraw(self, amount):
        self.money -= amount
        print(f'You withdraw from your bank account {amount} lei')
        print(f'Your balance is now:{self.money} lei')
    
    def benefits_user(self):
        print(
            '''
                    1. No fee taxes
                    2. No fee taxes for exchange
                    3. Custom name
                    4. Customer support
                    5. And a kiss on your hand
                    '''
            )


class ClassicAccount(Bank):
    def benefits_user(self):
        print(
            '''
                    1. You are just a simple human
                    2. You are not a king brush
                    3. You so poor
                    4. Customer support
                    5. Yeah go away poor
                    '''
            )


def main():
    name = name_user()
    date_of_birth = birth_user()
    account = type_account_user()
    if account == 'Premium':
        bank_account = PremiumAccount(money = 0, date_of_birth = date_of_birth, name = name, account = account)
    else:
        bank_account = ClassicAccount(money = 0, date_of_birth = date_of_birth, name = name, account = account)
    
    show_panel()
    try:
        while True:
            user_input = input('Press a number from the panel: ').strip()
            match user_input:
                case '1':
                    bank_account.info_user()
                case '2':
                    bank_account.check_balance()
                case '3':
                    bank_account.deposit(amount = user_amount())
                case '4':
                    bank_account.withdraw(amount = user_amount())
                case '5':
                    bank_account.benefits_user()
                case '6':
                    show_panel()
                case '7':
                    sys.exit('Goodbye')
    
    except ValueError:
        print('Sorry you need to try again ')


if __name__ == '__main__':
    main()
