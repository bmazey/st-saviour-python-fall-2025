from password import generate_password


def test_password_alpha_characters():
    # TODO BONUS ensure that the first 5 characters are letters
    password = "abcde1234!"
    assert password[:5].isalpha()

def test_password_numberic_characters():
    # TODO BONUS ensure the placement of the 4 digit characters
    password = "abcde1234!"
    assert password[5:9].isdigit()

def test_password_symbol_character():
    # TODO BONUS ensure the final character is a symbol
    password = "abcde1234!"
    assert password[-1] in '!@#$%^&*'

def test_password_length():
    # TODO BONUS ensure the length of the password is 10
    password = "abcde1234!"
    assert len(password) == 10

def test_password_unique():
    # HINT we ignore collisions for the purposes of this exercise
    # TODO BONUS create two passwords, and ensure they are distinct
    password1 = "abcde1234!"
    password2 = "fghij5678!"
    assert password1 != password2

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    return 1 in [c in s for c in collection]
