currency = {
    'USD': 1,
    'EUR': 0.89,
    'RON': 4.54,
    'GPD': 3.2

}


def first_currency():
    while True:
        currency1 = input('What currency do you want to start with: ').strip().upper()
        if currency1.isascii():
            if currency1 in currency:
                break
            else:
                print('Invalid choice!')
        else:
            print('Invalid choice!')
    return currency1


def second_currency():
    while True:
        currency2 = input('What currency do you want to finish with: ').strip().upper()
        if currency2.isascii():
            if currency2 in currency:
                break
            else:
                print('Invalid choice!')
        else:
            print('Invalid choice!')
    return currency2


def money():
    while True:
        money_user = input('Please insert how much money do you want to convert:').strip()
        if money_user.isdigit():
            money = int(money_user)
            break
        else:
            print('Invalid choice!')
    return money


print('Here are the conversion rate')
for key, value in currency.items():
    print(key, ':', value)

while True:

    amount = money()
    start_currency = first_currency()
    end_currency = second_currency()

    if start_currency in currency and end_currency in currency:
        conversion = float(amount * currency[end_currency] / currency[start_currency])
    print(f'The  conversion is {round(conversion, 2)} {end_currency}')
    new_conversion = input('Do you want to convert again? Press q to quit and enter to continue:')
    if new_conversion == 'q':
        print('Goodbye!')
        break
