def name_user():
	name = None
	while not name:
		name = input('What is your name: ').strip().capitalize()
	return name


def print_panel():


class BankAccount:
	def __init__(self, name, money, date_of_birth):
		self.name = name
		self.money = money
		self.date_of_birth = date_of_birth
	
	def show_user(self):
		print(f'''
		Name: {self.name}
		Date of birth:{self.date_of_birth}
		Money in deposit:{self.money}
		''')
	
	def check_balance(self):
		print(f'Your balance is: {self.money}')
	
	def withdraw(self, amount):
		self.money -= amount if amount > 0 else print('The amount must me greater then 0')
		return self.money
	
	def deposit(self, amount):
		self.money += amount if amount > 0 else print('The amount must me greater then 0')
		return self.money


class PremiumAccount(BankAccount):
	def __init__(self, ):


class ClassicAccount(BankAccount):
