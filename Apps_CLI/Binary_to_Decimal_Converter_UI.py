def get_binary_user():
    binary = None
    while not binary:
        binary = input('Put here the binary: ').strip()
    return binary


def binary_to_decimal(binary):
    num = int(binary, 2)
    return num


def user_choice():
    user_input = None
    while not user_input:
        user_input = input('Types yes to convert the binary to decimal or n/no to quit: ').strip().lower()
    return user_input in ['yes', 'y']


def main():
    while True:
        try:
            choice = user_choice()
            if choice:
                user_binary = get_binary_user()
                decimal_result = binary_to_decimal(user_binary)
                print(f'Here is your conversion: {decimal_result} ')
            else:
                print('Goodbye!')
                break
        except ValueError:
            print('Sorry, you need to put only 0 and 1.')


if __name__ == '__main__':
    main()
