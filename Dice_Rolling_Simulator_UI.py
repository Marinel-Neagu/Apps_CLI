import random


def dice():
    try:
        min_number = 2
        faces_dice = None
        while not faces_dice:
            faces_dice = int(input('How many faces do you want for this dice to have: '))
            while faces_dice < min_number:
                faces_dice = int(input(f'You can have at least {min_number} face!!: '))
            else:
                result = random.randint(min_number, faces_dice)
                print('You rolled:', result)
                break

        return result

    except ValueError:
        print('Sorry man, you have to put stack integer!!!')
    except AttributeError:
        print('Sorry man, you have to put stack integer!!!')
    except UnboundLocalError:
        print('Sorry man, you have to put stack integer!!!')
    except Exception:
        print('Sorry man this is fucked up, you have to call the TOP G!!')


def new_game():
    while True:
        play_again = input('Do you want to play again!: ')
        if play_again == 'yes' or play_again == 'y':
            main(prompt=True)
        elif play_again == 'no' or play_again == 'n':
            print('I hoped it worked,you nerdy dude!')
            break
        else:
            print('Sorry man, just type yes or no: ')


def main(prompt=False):
    choice = None
    if not prompt:
        while True:
            choice = input(f'Do you want to roll stack dice, just type yes or no?: ').lower()
            if choice == 'yes' or choice == 'y':
                dice()
                break
            elif choice == 'no' or choice == 'n':
                print('Ok, you are stack ... stack nerd!')
                break

            else:
                print('Sorry are stack child?: ')

    if prompt:
        return dice()

    return choice.lower() in ['yes', 'y']


user_name = input('Hi, tell me your name pls!: ').capitalize()
print(f'Hello, {user_name}!What are you doing?', end=' ')

if __name__ == '__main__':
    if main():
        new_game()
