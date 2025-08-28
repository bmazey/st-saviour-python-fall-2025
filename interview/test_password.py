from password import generate_password


def test_password_alpha_characters():
    # TODO ensure that the first 5 characters are letters
    pass

def test_password_numberic_characters():
    # TODO ensure the placement of the 4 digit characters
    pass

def test_password_symbol_character():
    # TODO ensure the final character is a symbol
    pass

def test_password_length():
    # TODO ensure the length of the password is 10
    pass

def test_password_unique():
    # HINT we ignore collisions for the purposes of this exercise
    # TODO create two passwords, and ensure they are distinct
    pass

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    return 1 in [c in s for c in collection]
