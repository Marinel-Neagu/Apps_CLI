import math


def add():
    while True:
        try:
            first_number = float(input('Enter your first number: '))
            second_number = float(input('Enter your second number: '))
            result = first_number + second_number
            print('Your addition is: ', result)
        except ValueError:
            print('You have to put just numbers')

        return result


def subtract():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number - second_number
    print('Your subtraction is: ', result)
    return result


def multiply():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number * second_number
    print('Your multiply is: ', result)
    return result


def divide():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number / second_number
    print('Your divide is: ', result)
    return result


def power():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number ** second_number
    print('Your power is: ', result)
    return result


def square_root():
    number = float(input('Enter your  number: '))
    result = math.sqrt(number)
    print('Your square root is: ', result)
    return result


def new():
    while main():
        main()

        if not main():
            print('Goodbye!')
            break


def main():
    operation = None
    while not operation:
        operation = int(input("Chose your operation, by typing a number from the list!: "))
        try:
            if operation == 1:
                add()
            elif operation == 2:
                subtract()
            elif operation == 3:
                multiply()
            elif operation == 4:
                divide()
            elif operation == 5:
                power()
            elif operation == 6:
                square_root()
        except ValueError:
            print('You have to put a integer pls!')
            operation = int(input("Choose again, pls!: "))
        except Exception:
            print("This a serious problem!")
            break


import math


def add():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number + second_number
    print('Your addition is: ', result)
    return result


def subtract():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number - second_number
    print('Your subtraction is: ', result)
    return result


def multiply():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number * second_number
    print('Your multiply is: ', result)
    return result


def divide():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number / second_number
    print('Your divide is: ', result)
    return result


def power():
    first_number = float(input('Enter your first number: '))
    second_number = float(input('Enter your second number: '))
    result = first_number ** second_number
    print('Your power is: ', result)
    return result


def square_root():
    number = float(input('Enter your  number: '))
    result = math.sqrt(number)
    print('Your square root is: ', result)
    return result


def new():
    while main():

        if not main():
            print('Goodbye!')
            break


def main():
    while True:
        operation = int(input("Chose your operation, by typing a number from the list!: "))
        try:
            if operation == 1:
                add()
            elif operation == 2:
                subtract()
            elif operation == 3:
                multiply()
            elif operation == 4:
                divide()
            elif operation == 5:
                power()
            elif operation == 6:
                square_root()
            else:
                print('Just chose from 1 to 6!')
        except ValueError:
            print('You have to put a integer pls!')

        except Exception:
            print("This a serious problem!")
            break

        new_calculation = input('Do you want to calculate again? Type [yes/no]').lower()
        return new_calculation in ['yes']


if __name__ == '__main__':

    choice = None

    print(f'''

    ****************************************************************
                               Basic calculator!!!                         
    ****************************************************************
                             To continue, press 1                       
                             To exit, press 2                    

''')

    while True:
        try:
            choice = int(input('Press here....: '))
            if choice == 2:
                print(f'Goodbye!')
                break
            elif choice == 1:
                print('Press one number from the list below!')
                print("Select operation:")

                print(f'''
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
                    5. Power
                    6. Square root

''')

                main()
                new()


            else:
                print('Please select just 1 and 2!: ')

        except ValueError:
            print("You have to put a integer!!!")

        except Exception:
            print('Sorry there was a problem!')
            break
