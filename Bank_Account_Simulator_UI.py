
import datetime
import random


def name_user():
	name = None
	while not name:
		name = input('What is your name: ').strip().capitalize()
	return name


def type_account():
	print('''
	Premium Account-price = 999.99 lei
	Classic Account-price = 69.99 lei''')
	while True:
		ask_user = input('Do you want to buy a Classic or Premium account? Write classic or premium: ').strip().lower()
		if ask_user in ['classic', 'premium']:
			match ask_user:
				case 'classic':
					return False
				case 'premium':
					return True
				case _:
					print('Invalid option')


def date_of_birth():
	print('We need your birthdate!')
	while True:
		try:
			user_year = input('In what year did you born?: ').strip()
			user_month = input('In what month did you born?: ').strip()
			user_day = input('In what day did you born?: ').strip()
			if datetime.datetime(year=int(user_year), month=int(user_month), day=int(user_day)):
				birth = f'{user_day}.{user_month}.{user_year}'
				return birth
			else:
				print('Invalid date!')
		except ValueError:
			print('Invalid date! Try again!!')


def money():
	user_money = input('Do you want deposit money in your first account? Type yes/y or no/n')
	if user_money in ['yes', 'y']:
		money_account = input('How much do you want to put in this account').strip()
		return int(money_account) if money_account.isdigit() else print('Sorry you need to put a number')
	else:
		return 0


class Bank:
	def __init__(self, rate=19):
		self.rate = rate / 100
		self.name = name_user()
		self.type_account = type_account()
		self.money = money()
		self.date_of_birth = date_of_birth()
		self.id = random.choice(range(123435))
	
	def show_user(self):
		print(f'''
		Name: {self.name}
		Date of birth:{self.date_of_birth}
		Money in deposit:{self.money}
		
		''')
	
	def check_balance(self):
		print(f'Your balance is: {self.money}')
	
	def withdraw(self, amount):
		self.money -= amount + self.rate if amount > 0 else print('The amount must be greater than 0')
		print(f'''
		You withdraw from your bank account {amount} lei
		You balance is now:{self.money}
		''')
	
	def deposit(self, amount):
		self.money += amount if amount > 0 else print('The amount must be greater than 0')
		print(f'You deposit in your bank account {self.money}')


class PremiumAccount(Bank):
	def withdraw(self, amount):
		self.money -= amount if amount > 0 else print('The amount must be greater than 0')
		print(f'You withdraw from your bank account {self.money}')

	def show_benefits(self):
		print('''
		1. No fee taxes
		2. No fee taxes for exchange
		3. Custom name
		4. Customer support
		''')
class Classic(Bank):
	def show_benefists(self):
		print('''
		1. No fee taxes
		2. No fee taxes for exchange
		3. Custom name
		4. Customer support
		''')

def main():
	while True:
	


if __name__ == '__main__':
	main()
