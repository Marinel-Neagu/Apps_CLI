def hello():
    while True:
        name = input('Hello, what is your name: ').capitalize().strip()
        if name.isdigit() or name == '':
            print('Please choose a valid name!')
        else:
            print(f'Hello {name}! Do you want to play a Tic Tac Toe match?')
            choice = input('Just press y to play and q to quit...').lower()
            break
    return choice in ['y', 'yes']


def board(i):
   print(f''' 
      {i[1]}|{i[2]}|{i[3]}
        ____|______|____
     {i[4]} |{i[5]}|{i[6]}
        ____|______|____
      {i[7]}|{i[8]}|{i[9]}
            |      | 
''')



def game():
    player1 = input('')


def main():
    if hello():
        game()
    else:
        print('Goodbye, see you later!')


if __name__ == '__main__':
    board(input(''))
