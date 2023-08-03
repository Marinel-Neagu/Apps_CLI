def user_first_number():  # Checking the first number
	while True:
		num1 = input('Please tell me a first number for the fibonacci series: ')
		try:
			num1 = int(num1)
			if num1 <= 0:
				print('You have to put a positive number!')
			else:
				break
		
		except ValueError:
			print('Please just put positive number!')
	return num1


def user_second_number():  # The player choose the second number, and it checks if is a number or not
	while True:
		num2 = input('Please tell me a second number for the fibonacci series: ')
		try:
			num2 = int(num2)
			if num2 < 0:
				print('You have to put a positive number and bigger than the first number you selected before: ')
			
			else:
				break
		except ValueError:
			print('Please just put  number bigger than 0!')
	return num2


def user_limit():  # The player choose the  limit for the sequence and check it
	limit = None
	while not limit:
		try:
			limit = int(input('Please tell me a limit  for the fibonacci series: '))
		except ValueError:
			print('Try again, you have to put just a number!')
	return limit


def fibonacci_sequence(): #
	a = user_first_number()
	b = user_second_number()
	limit = user_limit()
	fibonacci_list = [a, b]
	
	while True:
		try:
			if fibonacci_list[-1] + fibonacci_list[-2] <= limit:
				next_number = fibonacci_list[-1] + fibonacci_list[-2]
				fibonacci_list.append(next_number)
			else:
				break
		except ValueError:
			print('Sorry, this is not a good value!!')
	print('Here is you sequence: ', ', '.join(str(i) for i in fibonacci_list)) #  it iteration# for every number from
# the fibonacci_list, and it puts it together with a "," between them


def new_fibonacci_sequence(): # asking for a new fibonacci sequence
	while True:
		new_sequence = input('Do you want to try a new sequence? Just press yes or q to exit: ')
		if new_sequence == 'y' or new_sequence == 'yes':
			fibonacci_sequence()
		elif new_sequence == 'q' or new_sequence == 'quit':
			print("Goodbye,have a good day!")
			break


def main():
	fibonacci_sequence()
	new_fibonacci_sequence()


if __name__ == '__main__':
	main()
