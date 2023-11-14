import random
import os


def name_boy_list():
    """

    :return: the most popular names for the boys
    """
    list_of_name = [
            
            "Wade", "Dave", "Seth", "Ivan", "Riley", "Gilbert", "Jorge", "Dan", "Brian", "Roberto", "Ramon", "Miles",
            "Liam", "Nathaniel", "Ethan", "Lewis", "Milton", "Claude", "Joshua", "Glen", "Harvey", "Blake", "Antonio",
            "Connor", "Julian", "Aidan", "Harold", "Conner", "Peter", "Hunter", "Eli", "Alberto", "Carlos", "Shane",
            "Aaron", "Marlin", "Paul", "Ricardo", "Hector", "Alexis", "Adrian", "Kingston", "Douglas", "Gerald", "Joey",
            "Johnny", "Charlie", "Scott", "Martin", "Tristin", "Troy", "Tommy", "Rick", "Victor", "Jessie", "Neil",
            "Ted",
            "Nick", "Wiley", "Morris", "Clark", "Stuart", "Orlando", "Keith", "Marion", "Marshall", "Noel", "Everett",
            "Romeo", "Sebastian", "Stefan", "Robin", "Clarence", "Sandy", "Ernest", "Samuel", "Benjamin", "Luka",
            "Fred",
            "Albert", "Greyson", "Terry", "Cedric", "Joe", "Paul", "George", "Bruce", "Christopher", "Mark", "Ron",
            "Philip", "Jimmy", "Arthur", "Jaime", "Perry", "Harold", "Jerry", "Shawn", "Walter", "Craig"
            
            ]
    
    random_name = random.choice(list_of_name)
    return random_name


def surname_list():
    """

    :return:list of the most popular surname in English
    """
    list_of_name = [
            
            "Williams", "Harris", "Thomas", "Robinson", "Walker", "Scott", "Nelson", "Mitchell", "Morgan", "Cooper",
            "Howard", "Davis", "Miller", "Martin", "Smith", "Anderson", "White", "Perry", "Clark", "Richards",
            "Wheeler",
            "Warburton", "Stanley", "Holland", "Terry", "Shelton", "Miles", "Lucas", "Fletcher", "Parks", "Norris",
            "Newton", "Potter", "Francis", "Erickson", "Norman", "Moody", "Lindsey", "Gross", "Sherman", "Simon",
            "Jones",
            "Brown", "Garcia", "Rodriguez", "Lee", "Young", "Hall", "Allen", "Lopez", "Green", "Gonzalez", "Baker",
            "Perez",
            "Campbell", "Shaw", "Gordon", "Burns", "Warren", "Long", "Mcdonald", "Gibson", "Ellis", "Fisher",
            "Reynolds",
            "Jordan", "Hamilton", "Ford", "Graham", "Griffin", "Russell", "Foster", "Butler", "Simmons", "Flores",
            "Bennett", "Sanders", "Hughes", "Bryant", "Patterson", "Matthews", "Jenkins", "Watkins", "Ward", "Murphy",
            "Bailey", "Bell", "Cox", "Martinez", "Evans", "Rivera", "Peterson", "Gomez", "Murray", "Tucker", "Hicks",
            "Crawford", "Mason", "Rice", "Black", "Knight", "Arnold", "Wagner", "Mosby", "Ramirez", "Coleman", "Powell",
            "Singh", "Patel", "Wood", "Wright", "Stephens", "Erikson", "Cook", "Roberts", "Holmes", "Kennedy",
            "Saunders",
            "Fisher", "Hunter", "Reid", "Stewart", "Carter", "Phillips", "Spencer", "Howell", "Alvarez", "Little",
            "Jacobs",
            "Foreman", "Knowles", "Meadows", "Richmond", "Valentine", "Dudley", "Woodward", "Weasley", "Livingston",
            "Sheppard", "Kimmel", "Noble", "Leach", "Gentry", "Lara", "Pace", "Trujillo", "Grant", "Guzman", "Daniel",
            "Adams"]
    
    random_name = random.choice(list_of_name)
    return random_name


def name_girl_list():
    """

    :return:list of the most popular girl name in English
    """
    list_of_name = [
            
            'Olivia', 'Emma', 'Charlotte', 'Amelia', 'Sophia', 'Isabella', 'Ava', 'Mia', 'Evelyn', 'Luna', 'Harper',
            'Camila', 'Sofia', 'Scarlett', 'Elizabeth', 'Eleanor', 'Emily', 'Chloe', 'Mila', 'Violet', 'Penelope',
            'Aria',
            'Abigail', 'Ella', 'Avery', 'Hazel', 'Nora', 'Layla', 'Lily', 'Aurora', 'Nova', 'Ellie', 'Madison', 'Grace',
            'Isla', 'Willow', 'Zoe', 'Riley', 'Stella', 'Eliana', 'Ivy', 'Victoria', 'Emilia', 'Zoey', 'Naomi',
            'Hannah',
            'Lucy', 'Elena', 'Lillian', 'Maya', 'Leah', 'Paisley', 'Addison', 'Natalie', 'Valentina', 'Everly',
            'Delilah',
            'Leilani', 'Madelyn', 'Kinsley', 'Ruby', 'Sophie', 'Alice', 'Genesis', 'Claire', 'Audrey', 'Sadie',
            'Aaliyah',
            'Josephine', 'Autumn', 'Brooklyn', 'Quinn', 'Kennedy', 'Cora', 'Savannah', 'Caroline', 'Athena', 'Natalia',
            'Hailey', 'Aubrey', 'Emery', 'Anna', 'Iris', 'Bella', 'Eloise', 'Skylar', 'Jade', 'Gabriella', 'Ariana',
            'Maria', 'Adeline', 'Lydia', 'Sarah', 'Gianna']
    random_name = random.choice(list_of_name)
    return random_name


def title():
    print(
            '''
                
                
                
                
                '''
            )


def user_choice():
    print('Hello, do you want to generat a random name, press yes/y or no/n to quit')
    input_user = None
    while not input_user:
        input_user = input('Press here: ').strip().lower()
    return input_user in ['yes', 'y']


def print_panel():
    print(
            '''
                    1. Generate a simple name
                    2. Generate a surname name
                    3. Generate a full name
                '''
            )


def get_user_number():
    print('Please choose a number from the panel!')
    while True:
        number = input('Insert here the number: ').strip()
        if number.isdigit():
            number = int(number)
            if number in range(1, 4):
                return number
            else:
                print('Please choose a number from the panel! ')
        else:
            print('Please choose a number!')


def gender():
    print('Firstly, tell me what gender you are looking for. Type boy or girl.')
    while True:
        input_user = input('Insert here: ').strip().lower()
        if input_user in ['boy', 'girl']:
            return input_user
        else:
            print('Please type_account boy or girl')


def boy():
    print_panel()
    number = get_user_number()
    match number:
        case 1:
            print(f'Here is your name for the boy: {name_boy_list()}')
        case 2:
            print(f'Here is your surname for the boy: {surname_list()}')
        
        case 3:
            print(f'Here is your full name for the boy: {name_boy_list()} {surname_list()}')


def girl():
    print_panel()
    number = get_user_number()
    match number:
        case 1:
            print(f'Here is your name for the girl: {name_girl_list()}')
        case 2:
            print(f'Here is your surname for the girl: {surname_list()}')
        
        case 3:
            print(f'Here is your full name for the girl: {name_girl_list()} {surname_list()}')


def show_name():
    name_gender = gender()
    match name_gender:
        case 'boy':
            boy()
        case 'girl':
            girl()


def main():
    choice = user_choice()
    while True:
        if choice:
            show_name()
            new = input('Do you want to generate a new name?: ').strip().lower()
            if new in ['yes', 'y']:
                show_name()
            else:
                print('Goodbye')
                break
        else:
            print('Goodbye')
            break


if __name__ == '__main__':
    main()
