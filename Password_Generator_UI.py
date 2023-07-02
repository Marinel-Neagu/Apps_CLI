import random
import string

print('                            Password generator!!!                                     ')
print('                             Press yes to choose!                  ')

length_password = int(input('How long do you want the password?: ').lower().strip())
amount = int(input('How many passwords do you need?: ').lower().strip())

letters_upper = input('Do you want to add upper letters?: ').lower().strip()

letters_lower = input('Do you want to add lower letters?: ').lower().strip()
digits = input('Do you want to add digits?: ').strip().lower()
punctuations = input('Do you want to add punctuation?:').strip().lower()
x = ''

if letters_upper == 'y' or letters_uppere == ' yes':
    x += string.ascii_lowercase

if punctuations == 'y' or punctuations == ' yes':
    x += string.punctuation

if letters_lower == 'y' or letters_lower == ' yes':
    x += string.ascii_lowercase

if digits == 'y' or digits == ' yes':
    x += string.ascii_lowercase

print('________________________________________________________________________')

print('Your passwords are this!')
for i in range(amount):
    password = ''.join(random.sample(x, length_password))
    print(f'Password NO.{i} =', password)
