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
    digits = ''.join(random.choices(string.digits, k=4))
    symbol = random.choice('!@#$%^&*')

    return letters + digits + symbol