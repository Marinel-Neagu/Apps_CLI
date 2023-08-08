def currency1():
	while True:
		cur1 = input('Please chose the currency do you have:').strip().upper()
		if cur1 in currency:
			return cur1
		else:
			print('Please choose from the list!')


def currency2():
	while True:
		cur2 = input('Please chose the currency do you want to change to:').strip().upper()
		if cur2 in currency:
			return cur2
		else:
			print('Please choose from the list!')


def amount():
	number = input('Hi, please tell me how many money do you want to convert!')
	return number


currency = {'USD': 1, 'EUR': 0.92, 'RON': 4.54, 'GBP': 0.79}
for key, value in currency.items():
	print(key, ':', value)

while True:
	start_currency = currency1()
	end_currency = currency2()
	money = amount()
	if start_currency in currency and end_currency in currency:
		conversion = (currency[start_currency] * money) / currency[end_currency]
		
		print('Here is your value:', conversion)
		break
	else:
		print('Please choose a good one!')
