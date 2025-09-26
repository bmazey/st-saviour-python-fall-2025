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
    assert password[6].isdigit()
    assert password[7].isdigit()
    assert password[8].isdigit()

def test_password_symbol_character():
    # TODO BONUS ensure the final character is a symbol
    password = generate_password()
    assert not password[9]
    assert not password[9]

def test_password_length():
    # TODO BONUS ensure the length of the password is 10
    password = generate_password()
    assert len(password) == 10

def test_password_unique():
    # HINT we ignore collisions for the purposes of this exercise
    # TODO BONUS create two passwords, and ensure they are distinct
    first_password = generate_password()
    second_password = generate_password()
    assert not first_password == second_password

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    return 1 in [c in s for c in collection]
