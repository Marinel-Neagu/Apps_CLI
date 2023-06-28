def game():

    food = input("Give a food name: ")
    name1 = input("Give a character's name: ").capitalize()
    adjective = input("Give an adjective: ")
    noun = input("Give a noun: ")
    verb1 = input('Give a first action: ')
    verb2 = input('Give a second action: ')
    verb3 = input('Give a third action: ')
    print(
        '*********************************************************************************************************')

    text = f"""It was {food.lower()} day at school, and {name1} was super {adjective.lower()} for lunch.
    But when she went outside to eat, a {noun.lower()} stole her {food.lower()}! {name} chased the {noun.lower()} all over school.
    She {verb1.lower()}, {verb2.lower()}, and {verb3.lower()} through the playground.
    Then she tripped on her {noun.lower()} and the {noun.lower()} escaped! Luckily {name1}'s friends
    were willing to share their {food.lower()} with her."""
    print(text)


name = None
while not name:
    name = input('Hello, what is your name: ').capitalize()

decision = input(f'Hi, {name}! Do you want to play Mad Libs? Type yes or no: ').lower()
if  decision == "yes":
    game()

elif decision == "no":
    print('Goodbye, have a nice day!')

else:
    print('Sorry,something went wrong :( ')



