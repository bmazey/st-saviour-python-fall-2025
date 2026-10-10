from password import generate_password


def test_password_alpha_characters():
    # TODO BONUS ensure that the first 5 characters are letters
    pass 
    #alpha makes sure that 5 characters are letters (next 5 lines) 
    #creating password
    password = generate_password

    assert password[0].isalpha() 
    assert password[1].isalpha() 
    assert password[2].isalpha()  
    assert password[3].isalpha() 
    assert password[4].isalpha() 
    # add 5 random letters ...
   
def test_password_numberic_characters():
    # TODO BONUS ensure the placement of the 4 digit characters
    pass 

# digit makes sure that 4 characters are digits 
password = generate_password 
assert password[5].isdigit()
assert password[6].isdigit() 
assert password[7].isdigit()
assert password[8].isdigit()

def test_password_symbol_character():
    # TODO BONUS ensure the final character is a symbol
    pass
password = generate_password 

# symbol makes sure that last digit is a symbol 
assert password[9].issymbol()

def test_password_length()
    # TODO BONUS ensure the length of the password is 10
    pass 
test_password_length 

def test_password_unique():
    # HINT we ignore collisions for the purposes of this exercise
    # TODO BONUS create two passwords, and ensure they are distinct
    pass

def contains(s: str, collection: list):
    # check if any characters in collection are present in s
    return 1 in [c in s for c in collection]
