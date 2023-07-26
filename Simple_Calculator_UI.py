import math


# asking and checking for  the first number
def num1():
    while True:
        num = input('Enter your first number: ')
        if num.isdigit():
            num = float(num)
            return num
        else:
            print('You have to put a digit!')


# asking and checking for  the second number
def num2():
    while True:
        num = input('Enter your first number: ')
        if num.isdigit():
            num = float(num)
            return num
        else:
            print('You have to put a digit!')


# sum function
def add(first_number, second_number):
    result = first_number + second_number
    print('Your addition is: ', result)
    return result


def subtract(first_number, second_number):
    result = first_number - second_number
    print('Your subtraction is: ', result)
    return result


def multiply(first_number, second_number):
    result = first_number * second_number
    print('Your multiply is: ', result)
    return result


def divide(first_number, second_number):
    result = first_number / second_number
    print('Your divide is: ', result)
    return result


def power(first_number, second_number):
    result = first_number ** second_number
    print('Your power is: ', result)
    return result


def square_root(number):
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
            first_number = num1()
            second_number = num2()
            if operation == 1:
                add(first_number, second_number)
            elif operation == 2:
                subtract(first_number, second_number)
            elif operation == 3:
                multiply(first_number, second_number)
            elif operation == 4:
                divide(first_number, second_number)
            elif operation == 5:
                power(first_number, second_number)
            elif operation == 6:
                square_root(first_number)
        except ValueError:
            print('You have to put a integer pls!')

        except ZeroDivisionError:
            print('You can t divide by zero man')
        except Exception:
            print('Sorry this is bad')


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
