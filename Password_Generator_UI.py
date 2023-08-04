import random
import string

# Welcome message
print('                            Password generator!!!                                     ')
print('                             Press yes to choose!                  ')

# Constants for valid choices
YES_CHOICE = ['yes', 'y']
NO_CHOICE = ['n', 'no', 'quit', 'q']


# Function to handle yes/no choices
def choices(choice):
	if choice in YES_CHOICE:
		return True
	elif choice in NO_CHOICE:
		return False
	else:
		print('Please insert yes or no!')


# Function to input desired password length
def password_lenght():
	while True:
		length_pass = input('How long do you want the password?: ').strip()
		if length_pass.isdigit():
			length_pass = int(length_pass)
			return length_pass
		else:
			print('Please insert a number!')


# Function to input number of passwords
def password_amount():
	while True:
		numbers_of_passwords = input('How many passwords do you need?: ').strip()
		if numbers_of_passwords.isdigit():
			numbers_of_passwords = int(numbers_of_passwords)
			return numbers_of_passwords
		else:
			print('Please insert a number!')


# Function to ask about adding upper case letters
def upper():
	letters_upper = input('Do you want to add upper letters?: ').lower().strip()
	return choices(letters_upper)


# Function to ask about adding lower case letters
def lower():
	letters_lower = input('Do you want to add lower letters?: ').lower().strip()
	return choices(letters_lower)


# Function to ask about adding digits
def digit():
	digits = input('Do you want to add digits?: ').strip().lower()
	return choices(digits)


# Function to ask about adding punctuation
def punctuation():
	punctuations = input('Do you want to add punctuation?: ').lower().strip()
	return choices(punctuations)


# Function to generate a new set of passwords
def new_password_generator():
	while True:
		new_pass = input('Do you need a new set of passwords? Press yes to continue...')
		if new_pass in YES_CHOICE:
			password_generator()
		elif new_pass in NO_CHOICE:
			print('Goodbye, have a nice day!')
			break
		else:
			print('Please, insert y or no!')


# Main password generation function
def password_generator():
	try:
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
		print('Your passwords are as follows:')
		for i in range(amount):
			# Generate a random password by sampling characters from 'all_' with specified length
			password = ''.join(random.sample(all_, length_password))
			print(f'Password NO.{i + 1} =', password)
	except ValueError:
		print('Sorry, you need to choose a password that is less than')

if __name__ == '__main__':
	password_generator()
	new_password_generator()
