import time


def welcome():
	print('Welcome, you are a new owenr of a misterious game named,"The dark soul"')
	time.sleep(2)
	print('The game is from your grandpa, that died in a war that was almost 30 years ago')
	time.sleep(2)
	print('Now the game that he made is in your hand')
	time.sleep(2)
	print('You have to choose what to do it with! Or you give that game to your dad, or you open the game')
	print('To open it write open')
	time.sleep(2)
	game_choice = input('Press here...')
	return game_choice in ['open']


def game_world():
	while True:
		game_welcome = welcome()
		if game_welcome:
			print('You are throw away into a new world, you are now in the video game!')
			time.sleep(3)
			print('What are you doing now: Try to cry or looking at yourself--')
			world_choice = input('Press here...').strip().lower()
			if world_choice == 'cry' or world_choice == 'run':
				print('You are now like a baby boy, and nothing is happening but then...')
				time.sleep(3)
				print('You are seeing a woman that is in black and with blood in her hands')
				time.sleep(3)
				print('Do you want to ask the woman or run')
		
		else:
			print('Goodbye!')
			break


if __name__ == '__main__':
	game_world()
