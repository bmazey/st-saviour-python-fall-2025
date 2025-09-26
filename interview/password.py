import random
import string

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

    letters = ''.join(random.choices(string.ascii_lowercase, k=5))
    # this describes the letter string and generates 5 random lowercase letters
    digits = ''.join(random.choices(string.digits, k=4))
    # this describes the number string and generates 4 random numbers
    symbol = random.choice('!@#$%^&*')
    # this describes the symbol string and generates 1 random symbol
    return letters + digits + symbol
    # this combines all other strings into one string with 5 letters, 4 numbers, and 1 symbol
    

