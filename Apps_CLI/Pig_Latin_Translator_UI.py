import re


def ask_user():
    choice = None
    while not choice:
        choice = input("Do you want to translate a text to a pig latin? Press yes/y or no/n to quit: ").strip().lower()
    return choice in ['yes', 'y']


def get_sentence():
    sentence = None
    while not sentence:
        sentence = input('Write here the sentence: ').strip()
    return sentence


class PigTranslator:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def translate_word(self, word):
        
        pattern = r'(^[^AEIOUaeiou]+)?(.+)$'  # capture the letter that are not vowels, because i used the negation ^
        # inside the []
        pattern = re.match(pattern, word)
        first_letter, rest_of_word = pattern.groups()
        if pattern:
            if first_letter:
                pig_word = rest_of_word + first_letter + 'ay'
            else:
                print(first_letter)
                pig_word = rest_of_word + 'way'
            return pig_word
        else:
            print('sorry')
    
    def translate_sentence(self):
        text = self.sentence.split()
        translate = [self.translate_word(word) for word in text]
        return ' '.join(translate)


def main():
    while True:
        choice = ask_user()
        if choice:
            sentence = get_sentence()
            pig_translate = PigTranslator(sentence = sentence)
            print(
                f'''
			Original text:{pig_translate.sentence}
			Pig latin text: {pig_translate.translate_sentence()}'''
                )
        else:
            print('Goodbye!')
            break


if __name__ == '__main__':
    main()
