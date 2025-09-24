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

    # remember to import random so syntax error does not occur and the code can randomize a number
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print('the length of letters is: ' + str(len(letters)))
    r = random.randint(0, len(letters) - 1)
    print('the random int is: ' + str(r))
    print('the random letter is: ' + letters[r])

r = random.randint(0, len )

    return ''
