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

import random

# got this from google
def generate_password() -> str:
    lowercase_characters = "abcdefghijklmnopqrstuv" 
digits = "0123456789"
symbols = "!@#$^&*"
lowercase_characters = "abcdefghijklmnopqrstuv"
password_parts = [] 

def generate_password() -> str:
# also google
    for _ in range(5):
        password_parts.append(random.choice(lowercase_characters))
    for _ in range(4):
        password_parts.append(random.choice(digits))
    for _ in range(1):
        password_parts.append(random.choice(symbols))
        return "".join(password_parts)
    
if 2+2 == 4:
    password = generate_password()
    print (f"Generated Password: {password}")
    # f is for 'formatted string literal' (it printst out the actual answer instead of just 'password')