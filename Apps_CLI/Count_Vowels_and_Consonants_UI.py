# oop program
class countvowelsconsonants:
    def __init__(self, sentence):
        self.sentence = sentence.lower()
        self.vowels = 'aeiou'
        self.consonants = 'bcdfghjklmnpqrstvwxyz'
    
    def count_vowels(self):
        count_vowels = 0
        for letter in self.sentence:
            if letter in self.vowels:
                count_vowels += 1
        return count_vowels
    
    def count_consonants(self):
        count_consonants = 0
        for letter in self.sentence:
            if letter in self.consonants:
                count_consonants += 1
        return count_consonants


def sentence_user():
    sentence = None
    while not sentence:
        sentence = input('Insert here a sentence, or a word: ').strip()
    return sentence


def main():
    print('To quit insert quit below or just continue to use the program.')
    while True:
        sentence = sentence_user()
        if sentence != 'quit':
            counting = countvowelsconsonants(sentence = sentence)
            print(
                f'''
			total consonants: {counting.count_consonants()}
			total vowels: {counting.count_vowels()}
			'''
                )
        else:
            print('Goodbye!')
            break


if __name__ == '__main__':
    main()
#
## functional programimg
#
# def sentence_user():
# 	text = none
# 	while not text:
# 		text = input('insert here a text, or a word: ').lower()
# 	return text
#
#
# consonants = 'bcdfghjklmnpqrstvwxyz'
# vowels = 'aeiou'
#
# print('to quit insert quit below or just continue to use the program.')
# while true:
# 	counter_vowels, counter_consonants = 0, 0
# 	sentence = sentence_user()
# 	if sentence != 'quit':
# 		for letter in sentence:
# 			if letter in consonants:
# 				counter_consonants += 1
# 			if letter in vowels:
# 				counter_vowels += 1
# 		print(f'''
# 			 total consonants: {counter_consonants}
# 			 total vowels: {counter_vowels}''')
# 	else:
# 		print('goodbye!')
# 		break
