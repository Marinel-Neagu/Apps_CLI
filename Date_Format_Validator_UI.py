def get_time():
	"""

	:return:time from the user, and
	"""
	user_time = None
	while not user_time:
		user_time = input('Please put here a date to check it if it is good or not: ').strip()
	return user_time
	
	
	#
	# def checking_time():
	# 	while True:
	# 		initial_time = get_time()
	# 		valid_time = re.fullmatch(r'[0-9]+',initial_time)
	# 		if valid_time:
	# 			print('This date format is good!')
	# 		else:
	# 			print('Sorry this is bad')


def checking_time():










if __name__ == '__main__':
	checking_time()
