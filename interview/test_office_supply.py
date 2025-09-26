# Import the necessary functions from the 'office_supply' module.
from office_supply import staple_to_front, staple_to_end, shred_first_character, shred_last_character

# Define a function to test the 'stapler' functions.
def test_stapler():
    # Verify that the staple_to_front function works correctly.
    # The 'assert' keyword checks if a condition is true. If it's not, the test fails.
    # Test case: stapling 'p' to the front of 'anda' should result in 'panda'.
    assert staple_to_front('anda', 'p') == 'panda'
    # Test case: stapling 's' to the front of 'aviour' should result in 'saviour'.
    assert staple_to_front('aviour', 's') == 'saviour'

    # Verify that the staple_to_end function works correctly.
    # Test case: stapling 'a' to the end of 'pand' should result in 'panda'.
    assert staple_to_end('pand', 'a') == 'panda'
    # Test case: stapling 'r' to the end of 'saviou' should result in 'saviour'.
    assert staple_to_end('saviou', 'r') == 'saviour'

# Define a function to test the 'shredder' functions.
def test_shredder():
    # Verify that the shred_first_character function works correctly.
    # shredding the first character of 'ppanda' should result in 'panda'.
    assert shred_first_character('ppanda') == 'panda'
    #  the first character of 'ssaviour' should result in 'saviour'.
    assert shred_first_character('ssaviour') == 'saviour'

    # Verify that the shred_last_character function works correctly.
    # Test case: shredding the last character of 'pandax' should result in 'panda'.
    assert shred_last_character('pandax') == 'panda'
    # Test case: shredding the last character of 'saviourx' should result in 'saviour'
    assert shred_last_character('saviourx') == 'saviour'