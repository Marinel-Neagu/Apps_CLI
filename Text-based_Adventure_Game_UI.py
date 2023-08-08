import time

'''
the start of the game
'''


def choice_checking_valid():
	while True:
		answer = input('Your choice is:').strip().lower()
		if answer == ' ':
			print('Please enter a answer, do not let this question emtpy!')
		else:
			return answer


def welcome():
	print('Welcome, you are a new owner of a mysterious game named, “The dark soul.”')
	time.sleep(2)
	print('The game is from your grandpa, that died in a war that was almost 30 years ago.')
	time.sleep(2)
	print('Now the game that he made is in your hand!')
	time.sleep(2)
	print('You have to choose what to do it with! Or you give that game to your dad, or you open the game.')
	player_welcome = choice_checking_valid()
	time.sleep(2)
	
	return player_welcome


def enter_world():
	game_welcome = welcome()
	if game_welcome == 'open':
		print('You are thrown away into a new world, you are now in the video game!')
		time.sleep(3)
		print('What are you doing now: Start cry or watching the surrounding?')
		world_choice = choice_checking_valid()
		if world_choice == 'cry' or world_choice == 'run':
			print('You are now like a baby boy, and nothing is happening, but then ...')
			time.sleep(3)
			print('You are seeing a woman that is in black and with blood in her hands.')
			time.sleep(3)
			print('Do you want to ask the woman or run?')
	elif game_welcome == 'throw away':
		time.sleep(1)
		print('You throw away the game, now you hear something from it....')
		time.sleep(3)
		print('The sound is coming form the game that you throw in trash can')
		time.sleep(3)
		print('And you see.... a black man with yellow eyes....')
		time.sleep(2)
		print('He is in a black coat, what are you gonna do?   ')
		print('Are you gonna run to your dad or asking the man?')
	
	else:
		print('Goodbye!')


def meet_the_characters():
	print('ahhah')


if __name__ == '__main__':
	enter_world()
