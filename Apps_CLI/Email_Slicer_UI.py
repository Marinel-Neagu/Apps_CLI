import re


class Email:
    def __init__(self):
        self.user_email = None
        self.choice = self.ask_user()
    
    def ask_user(self):
        choice = None
        while not choice:
            choice = input('Do you want to see a slice of an email? Press yes/y or no/n: ').strip().lower()
        return choice in ['yes', 'y']
    
    def get_email(self):
        user_email = None
        while not user_email:
            user_email = input('Put here the email: ')
        return user_email
    
    def extract(self):
        self.user_email = self.get_email()
        pattern = r'^([a-zA-Z0-9_/+-]+)@([a-zA-Z0-9._/+-]+)\.([a-zA-Z]{2,5})$'
        email_found = re.match(pattern, self.user_email)
        if email_found:
            name, domain, tdl = email_found.groups()
            print(
                f'''
			  Here is the details about this email:
			  Name:{name}
			  Domain: {domain}
			  TDL:{tdl}'''
                )
        else:
            print("This email is invalid! ")


if __name__ == '__main__':
    while True:
        email = Email()
        if email.choice:
            email.extract()
        else:
            print('Goodbye, see you out there!')
            break
