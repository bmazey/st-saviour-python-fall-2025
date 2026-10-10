import random

def generate_password() -> str:
    """
    generate_password() takes no arguments and produces a string
    which meets the following password complexity requirements:
        - the length of the password is 10
        - the first 5 characters are lower case letters
        - the next 4 characters are digits [0-9]
        - the final character is a symbol [!@#$%^&*]
        - it's relatively uncommon to generate the same password twice 
    """

    # HINT you will require the use of a random number generator for this function
    # https://docs.python.org/3/library/random.html#random.randint

    # TODO implement generate_password function
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!@#$%^&*'

    password = ''

    # add 5 random letters ...
    r = random.randint(0, 25)
    password += letters[r]

    r = random.randint(0, 25)
    password += letters[r]

    r = random.randint(0, 25)
    password += letters[r] 

    r = random.randint(0, 25)
    password += letters[r]

    r = random.randint(0, 25)
    password += letters[r]

    # add 4 random digits ...
    r = random.randint(0, 9)
    password += digits[r]

    r = random.randint(0, 9)
    password += digits[r]

    r = random.randint(0, 9)
    password += digits[r]

    r = random.randint(0, 9)
    password += digits[r]

    # add one random symbol
    r = random.randint(0, 8)
    password += symbols[r] 

    return password

print(generate_password())
