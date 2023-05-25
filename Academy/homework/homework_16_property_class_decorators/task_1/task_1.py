# Task 1
# Create a class method named `validate`, which should be
# called from the `__init__` method to validate parameter
# email, passed to the constructor. The logic inside the
# `validate` method could be to check if the passed email
# parameter is a valid email string.

class Email:
    def __init__(self, address: str):
        if self.validate(address):
            self.address = address
        else:
            self.address = None
            print(f'<{address}> is NOT a valid email.')

    @classmethod
    def validate(cls, address: str) -> bool:
        try:
            # Ділимо на prefix та domain
            prefix, domain = address.split('@')
            # Перевіряємо, що '@' один і тільки один
            checked = address.count('@') == 1
            # Перевіряємо наявність крапки в домені таб що вна тільки одна і в потрібному місці
            checked &= '.' in domain[1:-1] and domain.count('.') == 1
            if checked:
                domain2 = domain.split('.')[1]
                # Перевіряємо мінімальну довжину закінчення доменної частини
                checked &= len(domain2) >= 2
            # Перевіряємо наявність літер в домені та мінімальну довжину
            checked &= any(letter.isalpha() for letter in domain) and 3 <= len(domain) <= 63
            # Перевіряємо допустимі символи в домені
            checked &= all((letter.isalpha() or letter.isdigit()
                            or letter == '.' or letter == '-') for letter in domain)
            # Перевіряємо допустиму довжину локальної частини
            checked &= 1<= len(prefix) <= 64
            # Перевіряємо перший і останній символи локальної частини
            checked &= (prefix[0].isalpha() and (prefix[-1].isalpha() or prefix[-1].isdigit()))
            # Перевіряємо допустимі символи в локальній частині
            checked &= all((letter.isalpha() or letter.isdigit()
                            or letter == '.' or letter == '-' or letter == '_') for letter in prefix[1:-1])
            for char in '-_.':
                # Перевіряємо чи нема в локальній частині два символи підряд
                checked &= all(prefix[s:s+2].count(char) <= 1 for s in range(len(prefix)-2))
            # Перевіряємо чи нема в доменній частині два тире підряд
            checked &= all(domain[s:s + 2].count('-') <= 1 for s in range(len(domain) - 2))
            return checked
        except BaseException as e:
            print(e.__class__, e)
            return False

    @classmethod
    def re_validate(cls, address: str) -> bool:
        import re
        try:
            email_validate_pattern = \
                "^[a-zA-Z0-9]+[-_.]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[-]?[a-zA-Z0-9]+\.[a-z]{2,}$"
            return bool(re.match(email_validate_pattern, address))
        except BaseException as e:
            print(e.__class__, e)
            return False

if __name__ == '__main__':
    emails = 'abc-d@mail.com', 'abc.def@mail.com', 'abc.def@mail.com',\
        'abc_def@mail.com', 'abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com',\
        'abc#def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', \
        'abc.def@mail.org', 'abc.def@mail.com', 'abc.def@mail.c', \
        'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com'

    for number, email in enumerate(emails, 1):
        print(f'{number}. ', end='')
        email_address = Email(email)
        if email_address.address:
            print(f'<{email_address.address}> is a valid email address.')
        if email_address.re_validate(email):
            print(f'   <{email_address.address}> is a valid email address (with re).')
        else:
            print(f'   <{email}> is NOT a valid email (with re).')
