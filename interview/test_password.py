from password import generate_password


def test_password_alpha_characters():
    # TODO BONUS ensure that the first 5 characters are letters
    # its saying that you need to develop a password that contais 5 letters 
    password = generate_password()
    assert password[0].isalpha()
    assert password[1].isalpha()
    assert password[2].isalpha()
    assert password[3].isalpha()
    assert password[4].isalpha()

def test_password_numeric_characters():
    # TODO BONUS ensure the placement of the 4 digit characters
    # its saying that you are continuing your password at index 5
    # the next 4 are going to be digits
    password  = generate_password()
    assert password[5].isdigit()
    assert password[6].isdigit()
    assert password[7].isdigit()
    assert password[8].isdigit()

def test_password_symbol_character():
    # TODO BONUS ensure the final character is a symbol
    # its saying that since you have to make a symbol you can prove something isnt more than it is
    # you are saying that the symbol is not a digit nor a letter for index 9 
    password  = generate_password()
    assert not password[9].isalpha()
    assert not password[9].isdigit()

def test_password_length():
    # TODO BONUS ensure the length of the password is 10
    # this will test if the password you are genrating is only 10 characters
    password = generate_password()
    assert len(password) == 10

def test_password_unique():
    # HINT we ignore collisions for the purposes of this exercise
    # TODO BONUS create two passwords, and ensure they are distinct
    # this is testing if one random password is equal to another random password
    # if it is something is wrong and you need to make it that two random passwords are different
    first_password = generate_password()
    second_password = generate_password()
    assert not first_password == second_password

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    # this  will see if the characters in c are represented in s
    return 1 in [c in s for c in collection]
