def first_number():
    while True:
        num1 = input('Please tell me a first number for the fibonacci series:')
        try:
            num1 = int(num1)
            if num1 <= 0:
                print(f'You have to put a positive number!')
            else:
                break

        except ValueError:
            print('Please just put positive number!')
    return num1


def second_number():
    while True:
        num2 = input('Please tell me a second number for the fibonacci series:')
        try:
            num2 = int(num2)
            if num2 < 0:
                print(f'You have to put a positive number and bigger the sum of the 2 number you selected before: ')

            else:
                break
        except ValueError:
            print('Please just put positive number!')
    return num2


def user_limit():
    limit = None
    while not limit:
        try:
            limit = int(
                input(f'Please tell me a limit  for the fibonacci series that is greater the sum of the 2 number '
                      f'that you selected '))
        except ValueError:
            print('Try again, you have to put just numbers!')
    return limit


def fibonacci():
    a = first_number()
    b = second_number()
    max_number = user_limit()
    fibonacci_list = [a, b]

    while True:
        try:
            if fibonacci_list[-1] + fibonacci_list[-2] <= max_number:
                next_number = fibonacci_list[-1] + fibonacci_list[-2]
                fibonacci_list.append(next_number)
            else:
                break
        except Exception:
            print('Sorry, this is an error!')
    print('Here is you sequence: ', ' '.join(str(i) for i in fibonacci_list))


def new():
    while True:
        new_sequence = input('Do you want to try a new sequence? Just press yes and q to exit:')
        if new_sequence == 'yes' or new_sequence == 'yes':
            fibonacci()
        elif new_sequence == 'q' or new_sequence == 'quit':
            print("Goodbye, cya later!")
            break


def main():
    fibonacci()
    new()


if __name__ == '__main__':
    main()
