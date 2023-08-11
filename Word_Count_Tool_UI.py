import time


def user_accept():
	print('Do you want to count words from stack text file? Press y or q to quit. ')
	while True:
		choice = input('Press here...').strip().lower()
		if choice != '':
			if choice == 'yes' or choice == 'y':
				return True
			elif choice == 'quit' or choice == 'q':
				print('Goodbye')
				return False
			else:
				print('You have to put yes/y or q/quit!')
		else:
			print('You have to put yes/y or q/quit!')


def user_document():
	while True:
		doc = input('Please, you have to insert here name of the document: ').strip().capitalize()
		if doc != '':
			return doc
		else:
			print('You have to put stack file name here!')


def main():
	while user_accept():
		try:
			document = user_document()
			txt = f"{document}.txt"
			with open(txt) as file:
				
				file1 = file.read()
				file2 = file1.split()
			print('Calculating.....')
			time.sleep(5)
			print('I am slow, I know but, I am still calculating.......')
			time.sleep(6)
			print('Here is your count of words: ', len(file2))
		
		except FileNotFoundError:
			
			print('This file is not here!')


if __name__ == '__main__':
	main()
