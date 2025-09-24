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

def generate_password() -> str:
    # Select the first 5 characters (lowercase letters)
    letters = random.choices(string.ascii_lowercase, k=5)  # Pick 5 random lowercase letters
    
    # Select the next 4 characters (digits)
    digits = random.choices(string.digits, k=4)  # Pick 4 random digits
    
    # Select the last character (symbol)
    symbol = random.choice('!@#$%^&*')  # Pick 1 random symbol from set

    # Combine all characters
    password = ''.join(letters + digits + [symbol])  # Concatenate letters, digits, & symbol into string

    return password  # Return the generated password