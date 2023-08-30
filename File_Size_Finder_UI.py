import os


def get_file():
	file_name = None
	while not file_name:
		file_name = input('What is the name of the file you want to see the file size: ').strip()
	return file_name


def show_file_size(file):
	size = os.path.getsize(f'{file}')
	return size


def user_choice():
	user_input = None
	while not user_input:
		user_input = input('Types yes to find a file size or n/no to quit: ').strip().lower()
	return user_input in ['yes', 'y']


def main():
	while True:
		try:
			choice = user_choice()
			if choice:
				file_name = get_file()
				file_size = show_file_size(file_name)
				print(f'The size of the file is:{file_size} bytes')
			else:
				print('Goodbye!')
				break
		except FileNotFoundError:
			print('Sorry, this file is not here or the name is wrong!')


if __name__ == '__main__':
	main()
