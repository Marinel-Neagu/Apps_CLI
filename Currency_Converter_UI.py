currency = {
    'USD': 1,
    'EUR': 0.92,
    'RON': 4.54,
    'GBP': 0.79
}
for key, value in currency.items():
    print(key, ':', value)
print('Hi, please tell me how many money do you want to convert!')
money = int(input('Please press here the sum:').strip())
start_currency = input('Please chose the currency do you have:').strip().upper()
end_currency = input('Please chose the currency do you to tranform:').strip().upper()

if start_currency in currency and end_currency in currency:
    conversion = (currency[start_currency] * money)/currency[end_currency]

    print('Here is your value:', conversion)
else:
    print('Please choose a good one!')
