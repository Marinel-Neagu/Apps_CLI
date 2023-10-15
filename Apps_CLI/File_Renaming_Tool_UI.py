import os


def get_user_filename():
	file_name = None
	while not file_name:
		file_name = input('Please insert the name of the file: ').strip()
	return file_name


def get_user_new_name():
	file_name = None
	while not file_name:
		file_name = input('Please insert a name that you want to see for the file: ').strip()
	return file_name


def rename_file(old_file_name, new_file_name):
	os.rename(f'test_folder/{old_file_name}.txt', f'test_folder/{new_file_name}.txt')


def main():
	try:
		while True:
			request = input('Do you want to rename a file? Press space to continue or no to quit: ').strip().lower()
			if request != 'no':
				old_file_name = get_user_filename()
				new_file_name = get_user_new_name()
				rename_file(old_file_name, new_file_name)
			else:
				print('Goodbye!')
				break
	except FileNotFoundError:
		print('File is not here!')


if __name__ == '__main__':
	main()
