import re

time_pattern = {'DD': r'\d{2}', 'MM': r'\d{2}', 'YYYY': r'\d{4}'}


def get_time():
	"""

	:return:time from the user, and
	"""
	user_time = None
	while not user_time:
		user_time = input('Please put here a date to check it if it is good or not: ').strip()
	return user_time


def get_format():
	type_data = None
	while not type_data:
		type_data = input('Please tell me what the format do you want to check: ')
	return type_data


def format_time_re():
	format_time = get_format()
	for key, value in time_pattern.items():
		format_time = re.sub(key, value, format_time)
		print(format_time)
	return format_time


def checking_time():
	user_time = get_time()
	pattern = format_time_re()
	print(pattern)
	valid_format = re.match(pattern, user_time)
	
	if valid_format:
		print('The format for the date you provide is good! ')
	else:
		print('The format is not a valid.')


if __name__ == '__main__':
	format_time_re()
