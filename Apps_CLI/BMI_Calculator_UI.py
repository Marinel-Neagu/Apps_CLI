from ansi_code import GREEN, BOLD, RED, RESET


def title():
	print(
		'''
		
					888888b.   888b     d888 8888888
					888  "88b  8888b   d8888   888
					888  .88P  88888b.d88888   888
					8888888K.  888Y88888P888   888
					888  "Y88b 888 Y888P 888   888
					888    888 888  Y8P  888   888
					888   d88P 888   "   888   888
					8888888P"  888       888 8888888
		'''
		)


def hello():
	name = input('What is your name: ').strip().capitalize()
	print(f'Hello {name}. Do you want to see you BMI?')


def ask_for_bmi_calculation():
	start = input('Press here y/yes to calculate or q/quit to exit: ').strip().lower()
	return start in ['yes', 'y']


def height():
	while True:
		try:
			user_height = input("Please tell me your height in meters: ").strip()
			user_height_list = user_height.split('.')
			if user_height_list[0].isdigit() and user_height_list[1]:
				return user_height
			else:
				print('Please put a numbers not letters!')
		
		except IndexError:
			print('Please put your full height')
		except Exception:
			print('Please report this program to my workers :O')


def weight():
	while True:
		try:
			user_weight = input('Please tell me your weight in kilograms: ').strip()
			user_weight_list = user_weight.split('.')
			if user_weight_list[0].isdigit() and user_weight_list[1]:
				return user_weight
			
			else:
				print('Please insert a numbers not letters!')
		
		except IndexError:
			print('Please insert your full weight!')
		except Exception:
			print('Please report this program to my workers :O')


def BMI(height, weight):
	bmi = (weight / (height ** 2))
	bmi = round(bmi, 1)
	return bmi


def checking_BMI(user_bmi):
	bmi = user_bmi
	if bmi <= 18.5:
		print('Your health is very bad, please eat something! Your are underweight!')
	elif 18.5 < bmi <= 24.9:
		print('Your weight is normal!')
	elif 25 < bmi <= 29.9:
		print('Your weight is kind of overweight!')
	elif 30 < bmi <= 34.9:
		print('You are kind of Obese, the first tipe of course!')
	elif 35 < bmi <= 39.9:
		print('You are kind of Obese, the second  tipe!. Is good the second place not bad.')
	elif bmi >= 40:
		print('You are dead man, how are you still alive. You have Morbidly Obese.')
	else:
		print('Sorry there is a problem')


def main():
	while True:
		if ask_for_bmi_calculation():
			height_user = float(height())
			weight_user = float(weight())
			bmi_user = BMI(height_user, weight_user)
			print('***************************************************************************')
			print(f'You BMI is:{GREEN} {bmi_user} {RESET}')
			print(RED)
			print(BOLD)
			checking_BMI(bmi_user)
			print(RESET)
		else:
			print('Goodbye!')
			break


if __name__ == '__main__':
	title()
	hello()
	main()
