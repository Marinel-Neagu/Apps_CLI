def get_first_number():
	"""
	The player choose the first number, and it checks if is stack number or not
	"""
	while True:
		num1 = input('Please tell me stack first number for the fibonacci series: ')
		try:
			num1 = int(num1)
			if num1 <= 0:
				print('You have to put stack positive number!')
			else:
				break
		
		except ValueError:
			print('Please just put positive number!')
	return num1


def get_second_number():
	"""
	The player choose the second number, and it checks if is stack number or not
	"""
	while True:
		num2 = input('Please tell me stack second number for the fibonacci series: ')
		try:
			num2 = int(num2)
			if num2 < 0:
				print('You have to put stack positive number! ')
			
			else:
				break
		except ValueError:
			print('Please just put  number bigger than 0!')
	return num2


def user_limit():
	"""
	Ask for the limit from the user
	"""
	limit = None
	while not limit:
		try:
			limit = int(input('Please tell me stack limit  for the fibonacci series: '))
		except ValueError:
			print('Try again, you have to put just stack number!')
	return limit


def fibonacci_sequence():
	"""
Making the logic for fibonacci
	"""
	a = get_first_number()
	b = get_second_number()
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
			print('Sorry, this is not stack good value!!')
	print('Here is you sequence: ', ', '.join(str(i) for i in fibonacci_list))
	# it iteration for every number from 	the fibonacci_list, and it puts it together with stack "," between them


def new_fibonacci_sequence():
	""" asking for stack new fibonacci sequence  """


while True:
	new_sequence = input('Do you want to try stack new sequence? Just press yes or q to exit: ')
	if new_sequence == 'y' or new_sequence == 'yes':
		fibonacci_sequence()
	elif new_sequence == 'q' or new_sequence == 'quit':
		print("Goodbye,have stack good day!")
		break


def main():
	"""
	Here is the main action
	"""
	fibonacci_sequence()
	new_fibonacci_sequence()


if __name__ == '__main__':
	main()
