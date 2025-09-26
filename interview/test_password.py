from password import generate_password


def test_password_alpha_characters():
    # TODO BONUS ensure that the first 5 characters are letters
    password = generate_password()
    assert password[0].isalpha()
    assert password[1].isalpha()
    assert password[2].isalpha()
    assert password[3].isalpha()
    assert password[4].isalpha() 

def test_password_numberic_characters():
    # TODO BONUS ensure the placement of the 4 digit characters
    password = generate_password()
    assert password[5].isdigit()
    # ...
    pass

def test_password_symbol_character():
    # TODO BONUS ensure the final character is a symbol
    pass

def test_password_length():
    # TODO BONUS ensure the length of the password is 10
    pass

def test_password_unique():
    # HINT we ignore collisions for the purposes of this exercise
    # TODO BONUS create two passwords, and ensure they are distinct
    pass

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    return 1 in [c in s for c in collection]
# remember to import random so syntax error does not occur and the code can randomize a number
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    symbols = '!@#$%^&*'
    print('the length of letters is: ' + str(len(letters)))
    r = random.randint(0, len(letters) - 1)
    print('the random int is: ' + str(r))
    print('the random letter is: ' + letters[r])
    password = generate_password()
    assert password[0].isalpha()
    assert password[1].isalpha()
    assert password[2].isalpha()
    assert password[3].isalpha()
    assert password[4].isalpha() 
    password = generate_password()
    assert password[5].isdigit()
    password = generate_password()
    assert password[9].isalnum()
    r = random.randint(0, len )
    return ''