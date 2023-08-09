import time

MOVES = ['left', 'right', 'forward', 'backward']
YES = ['yes', 'y']
NO = ['no', 'n', 'quit', 'q']


def back():
	print('You smell that someting is not ok with this, so you are running back.')
	time.sleep(2)
	print('You see a car, and guess what. Is one of your friend. And you go home')
	time.sleep(2)
	print('Goodbye!')


def win():
	print('You won the game and find the treasure, but you hear the an angel and try to run with the gold')
	time.sleep(2)
	print('You are still running and running, after a while you are hit by a car, and you try to get in.')
	time.sleep(1)
	print('The drive try to help you and he take away with him')
	time.sleep(1)
	print('Now you are fine, and happy. Goodbye')


def loss():
	print('You lost, you coult not escape.')
	time.sleep(3)
	print('You are being eaten by the angel, and sadly you die trying to pray!!!')
	time.sleep(2)
	print('Goodbye')


def user_answer():
	while True:
		user = input('Insert here your choice: ').strip().lower()
		if user in MOVES:
			return user
		else:
			print('Please an insert a valid choice')


def start_game():
	valid_choice = YES + NO
	print('Hello, do you want to play a text adventure game?')
	while True:
		user_start = input('Type yes or no, or to quit press q/quit:').strip().lower()
		if user_start in valid_choice:
			if user_start in YES:
				return True
			elif user_start in NO:
				return False


def enter_house():
	print('You are in front of a house, and you see a door, and you enter the house, and you see two different doors.')
	time.sleep(2)
	print('The left door is very old and black, and the right one is new and very bright.')
	time.sleep(2)


def left_door():
	print('You choose the left door, and you try to open it, but some bats are flying away from you.')
	time.sleep(2)
	print('You hear someone who is speaking in a wired language and he disperser.')
	time.sleep(2)
	print(
		'Now, you see a weird thing, like something is dead. What are you going, are you moving forward or backward. ')


def right_door():
	print("You choose the right door, and you are seeing an angel, that is telling you that can give you 3 wished "
	      "if you are moving forward to her.")
	time.sleep(2)
	print('You are looking at her and you are think if this is to nice to be true')
	time.sleep(2)


def treasure():
	print('You are near the dead thing and you see that something shining.')
	time.sleep(3)
	print('IT IS A TREASURE, YOU GRAB IT AND YOU LEFT WITH IT')
	time.sleep(3)


def angel():
	print('You are movign forward to the angel, but it is a trap....')
	time.sleep(3)
	print('The angel is not a good one, is a monster that eats people, and you are trying to escape. But it is '
	      'useless')
	time.sleep(2)


def main():
	start = start_game()
	if start:
		enter_house()
		if user_answer() == 'left':
			left_door()
			left_answer = user_answer()
			if left_answer == 'forward':
				treasure()
				win()
			elif left_answer == 'backward':
				back()
		elif user_answer() == 'right':
			right_door()
			right_answer = user_answer()
			if right_answer == 'forward':
				angel()
				loss()
			elif right_answer == 'backward':
				back()
			else:
				print('Please just insert forward or backward')
	
	else:
		print('Goodbye, have a nice day!')


if __name__ == '__main__':
	main()
