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

    letters ='abcdefghijklmnopqrstuvwxyz' 
    numbers = '0123456789'
    symbols = '!@#$%&*'
    
    password = ''
    r = random.randint(0, len(letters) - 1)
    password += letters[r]

    r = random.randint(0, len(letters) - 1)
    password += letters[r]

    r = random.randint(0, len(letters) - 1)
    password += letters[r]

    r = random.randint(0, len(letters) - 1)
    password += letters[r]

    r = random.randint(0, len(letters) - 1)
    password += letters[r]

    
   # now do numbers
    r = random.randint(0, len(numbers) - 1)
    password += numbers[r]

    r = random.randint(0, len(numbers) - 1)
    password += numbers[r]

    r = random.randint(0, len(numbers) - 1)
    password += numbers[r]

    r = random.randint(0, len(numbers) - 1)
    password += numbers[r]

    # now do symbols
    r = random.randint(0, len(symbols) - 1)
    password += symbols[r]

    return password

print('my password is: ' + generate_password())
