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
    
    # this gives the program something to refrence when trying yo make the code
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    symbols = '!@#$%^&*'

    # since the first objective is to code a password with 5 lowercase letters we have to allow the code to generate 5 random numbers
    # there should be 5 seperate pieces of code for the letters
    # we could do that by using the random string and the length of the total amount of letters in the alphabet
    # we could subtract 1 because the index starts at 0 so when we would get to the 26th letter it would be at the 25th index
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

    # the code can make the numbers now 
    # since we need to generate 4 random numbers we would do 4 differnt pieces of code for the numbers
    # we would use the random string and len of the single numbers starting at 0 and ending at 9 
    # we would have to subtract 1 since there are 10 number and only 9 indexes starting with zero
    r = random.randint(0, len(numbers) - 1)
    password += numbers[r]

    r = random.randint(0, len(numbers) - 1)
    password += numbers[r]

    r = random.randint(0, len(numbers) - 1)
    password += numbers[r]

    r = random.randint(0, len(numbers) -1)
    password += numbers[r]

    # allow the code to make symbol
    # we only need one piece of code since there only needs to be one symbol 
    # we would use the random string to get a random symbol
    # we would use the len to tell the code to use all the symbols given
    # we would subtract 1 since there will always be one less index of the actual number of symbols
    r = random.randint(0, len(symbols) - 1)
    password += symbols[r]

    return password

print('my password is: ' + generate_password())
