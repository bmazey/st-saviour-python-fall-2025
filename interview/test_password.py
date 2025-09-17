import string
from password import generate_password

def test_password_alpha_characters():
    password = generate_password()
    assert password[:5].isalpha(), "First 5 characters should be alphabetic"

def test_password_numberic_characters():
    password = generate_password()
    assert password[5:9].isdigit(), "Characters 6 to 9 should be digits"

def test_password_symbol_character():
    password = generate_password()
    symbols = string.punctuation
    assert password[-1] in symbols, "Last character should be a symbol"

def test_password_length():
    password = generate_password()
    assert len(password) == 10, "Password length should be 10"

def test_password_unique():
    password1 = generate_password()
    password2 = generate_password()
    assert password1 != password2, "Passwords should be unique"