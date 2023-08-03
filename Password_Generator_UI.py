import random
import string

print('                            Password generator!!!                                     ')
print('                             Press yes to choose!                  ')

YES_CHOICE = ['yes', 'y']
NO_CHOICE = ['n', 'no', 'quit', 'q']


def choices(type):
	if type == 'yes' or type == 'y':
		return True
	elif type == 'no' or type == 'n':
		return False
	else:
		print('Please insert yes or no!')


def password_lenght():
	while True:
		length_pass = input('How long do you want the password?: ').strip()
		if length_pass.isdigit():
			length_pass = int(length_pass)
			return length_pass
		else:
			print('Please insert a number!')


def password_amount():
	while True:
		numbers_of_passwords = input('How many passwords do you need?: ').strip()
		if numbers_of_passwords.isdigit():
			numbers_of_passwords = int(numbers_of_passwords)
			return numbers_of_passwords
		else:
			print('Please insert a number!')


def upper():
	letters_upper = input('Do you want to add upper letters?: ').lower().strip()
	choices(letters_upper)


def lower():
	letters_lower = input('Do you want to add lower letters?: ').lower().strip()
	choices(letters_lower)


def digit():
	digits = input('Do you want to add digits?: ').strip().lower()
	choices(digits)


def punctuation():
	punctuations = input('Do you want to add punctuation?: ').lower().strip()
	choices(punctuations)


def new_password_generator():
	while True:
		new_pass = input('Do you need a new set of password? Press yes to continue...')
		if new_pass == 'yes' or new_pass == 'y':
			password_generator()
			break
		else:
			print('Goodbye!')


def password_generator():
	all_ = ''
	amount = password_amount()
	length_password = password_lenght()
	if upper():
		all_ += string.ascii_uppercase
	
	if lower():
		all_ += string.ascii_lowercase
	
	if digit():
		all_ += string.digits
	
	if punctuation():
		all_ += string.punctuation
	
	print('________________________________________________________________________')
	print('Your passwords are this!')
	for i in range(amount):
		# Generate a random password by sampling characters from 'x' that is a list  of length 'length_password'
		password = ''.join(random.sample(all_, length_password))
		print(f'Password NO.{i + 1} =', password)


if __name__ == '__main__':
	password_generator()
	new_password_generator()
