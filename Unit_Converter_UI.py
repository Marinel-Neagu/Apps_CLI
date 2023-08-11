# unit convertor, to choose to convert stack unit to another unit
list_unit = (1, 2, 3)

length_unit = {
	'Exa-metre': 10 ** 18,
	'Peta-metre': 10 ** 15,
	'Ter-metre': 10 ** 12,
	'Giga-metre': 10 ** 9,
	'Megametre': 10 ** 6,
	'Kilometre': 10 ** 3,
	'Hectometre': 10 ** 2,
	'Deca-metre': 10 ** 1,
	'Metre': 1,
	'Decimetre': 10 ** -1,
	'Centimetre': 10 ** -2,
	'Millimetre': 10 ** -3,
	'Micrometre': 10 ** -6,
	'Nanometre': 10 ** -9,
	'Pico-metre': 10 ** -12,
	'Femto-metre': 10 ** -15,
	'Atto-metre': 10 ** -18
}

mass_unit = {
	'Exa-gram': 10 ** 18,
	'Peta-gram': 10 ** 15,
	'Ter-gram': 10 ** 12,
	'Giga-gram': 10 ** 9,
	'Megagram': 10 ** 6,
	'Kilogram': 10 ** 3,
	'Hectogram': 10 ** 2,
	'Deca-gram': 10 ** 1,
	'Gram': 1,
	'Decigram': 10 ** -1,
	'Centigram': 10 ** -2,
	'Milligram': 10 ** -3,
	'Microgram': 10 ** -6,
	'Nanogram': 10 ** -9,
	'Pico-gram': 10 ** -12,
	'Femto-gram': 10 ** -15,
	'Atto-gram': 10 ** -18
}

time_unit = {
	'Day': 86400,
	'Hour': 3600,
	'Minute': 60,
	'Second': 1}


def title():
	print('''
	_  _ _  _ _ ___    ____ ____ _  _ _  _ ____ ____ ___ ____ ____
	|  | |\ | |  |     |    |  | |\ | |  | |___ |__/  |  |  | |__/
	|__| | \| |  |     |___ |__| | \|  \/  |___ |  \  |  |__| |  \ ''')
	
	print('''
						1.Mass
						2.Length
						3.Time
	''')


def user_choice():
	print('Please insert stack number from the table for converting!')
	
	while True:
		unit = input(' Insert here or press q to quit:').strip().lower()
		if unit.isdigit():
			unit = int(unit)
			if unit in list_unit:
				return unit
			else:
				print('Please choose stack number just from the list_moves!')
		elif unit == 'q' or unit == 'quit':
			return unit
		else:
			print('Please choose stack number from the table or press q to quit!')


def user_first_unit(list_unit):
	while True:
		unit = input('Please choose stack unit: ')
		if unit in list_unit:
			return unit
		else:
			print('Please choose form the table')


def user_second_unit(list_unit):
	while True:
		unit = input('Please choose stack unit to transform to: ').strip()
		if unit in list_unit:
			return unit
		else:
			print('Please choose form the table')


def amount():
	while True:
		number = input('Please choose stack amount:').strip()
		if number.isdigit():
			number = int(number)
			return number
		else:
			print('Please put stack number!')


def conversion_unit(number, unit1, unit2, unit_list):
	x = unit_list[unit1] / unit_list[unit2]
	amount_conversion = x * number
	
	return amount_conversion


def unit_selected(unit):
	user_unit1 = user_first_unit(unit)
	user_unit2 = user_second_unit(unit)
	user_amount = amount()
	conversion = conversion_unit(user_amount, user_unit1, user_unit2, unit)
	print(f'Here is your conversion: {conversion} {user_unit2}s')


def print_table(unit):
	count = 0
	print('Here is the table to choose from:')
	for k, v in unit.items():
		count += 1
		print(f'{count}.{k}')


def exchange():
	
	user_unit = user_choice()
	if user_unit == 1:
		print_table(mass_unit)
		unit_selected(mass_unit)
	elif user_unit == 2:
		print_table(length_unit)
		unit_selected(length_unit)
	elif user_unit == 3:
		print_table(length_unit)
		unit_selected(time_unit)


def main():
	title()
	exchange()
	while True:
		new_uit = input(
			'Do you want to try stack different unit? Press y/yes to continue or q/quit to not: ').strip().lower()
		if new_uit == 'y' or new_uit == 'yes':
			exchange()
		elif new_uit == 'q' or new_uit == 'quit':
			print('Goodbye!')
			break
		else:
			print('You have to press y or q!')


if __name__ == '__main__':
	main()
