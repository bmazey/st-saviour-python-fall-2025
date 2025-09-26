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

    # HINT you will require the use of a random number generator for this function
    # https://docs.python.org/3/library/random.html#random.randint

    # Generate the 5 lowercase letters
    letters = string.ascii_lowercase
    password_part1 = "".join(random.choices(letters, k=5))

    # Generate the 4 digits
    digits = string.digits
    password_part2 = "".join(random.choices(digits, k=4))

    # Generate the 1 symbol
    symbols = "!@#$%^&*"
    password_part3 = random.choice(symbols)

    # Concatenate the parts to form the final password
    return password_part1 + password_part2 + password_part3

# Example usage:
# password = generate_password()
# print(password)