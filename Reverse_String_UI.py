def revers_string(string):
	return string[::-1]


def get_user_string():
	user_string = None
	while not user_string:
		user_string = input('Insert a text: ')
	return user_string


def user_choice():
	choice = None
	print('Please tell me if you want to see a reverse text press yes/y or no/n to quit. ')
	while not choice:
		choice = input('Press here: ').strip().lower()
	return choice in ['yes', 'y']


def main():
	while True:
		if user_choice():
			user_string = get_user_string()
			print(f'Here is your reversed string:{revers_string(user_string)}')
		else:
			print('Goodbye!')
			break


if __name__ == '__main__':
	main()
