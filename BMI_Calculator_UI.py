def title():
    pass


def hello():
    name = input('What is you name').strip().capitalize()
    print(f'Hello {name}. Do you want to see you BMI?')
    start = input('Press here y/yes to calculate or q/quit to exit')
    return start in ['yes', 'y']


def height():
    try:
        user_height = input("Please tell me your height in meters: ").strip()
        user_height_list = user_height.split('.')
        if user_height_list[0].isdigit() and user_height_list[1]:
            user_height_list[0] = int(user_height_list[0])
            user_height_list[1] = int(user_height_list[1])
            return user_height_list
        else:
            print('Please insert a numbers not letters!')

    except IndexError:
        print('Please insert your full height')
    except Exception:
        print('Please report this program to my workers :O')


def weight():
    try:
        user_height = input('Please tell me your weight in kilograms: ').strip()
        user_height_list = user_height.split('.')
        if user_height_list[0].isdigit() and user_height_list[1]:
            user_height_list[0] = int(user_height_list[0])
            user_height_list[1] = int(user_height_list[1])
            return user_height_list
        else:
            print('Please insert a numbers not letters!')

    except IndexError:
        print('Please insert your full weight!')
    except Exception:
        print('Please report this program to my workers :O')

def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi


def main():
    hello_user = hello()
    while True:
        if hello_user :
            height_user=height()
            weight_user=weight()
            print('You BMI is:',BMI(height_user,weight_user))
    pass


if __name__ == '__main__':
    main()
